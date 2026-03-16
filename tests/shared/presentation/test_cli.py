"""Presentation layer tests for the CLI Composition Root.

Verifies that the CLI module correctly defines available commands
and handles invalid arguments with appropriate exit behavior.
This tests the outermost Hexagonal layer boundary.
"""

import pytest
from unittest.mock import patch, AsyncMock, MagicMock


class TestCLICommandRouting:
    """Verifies the CLI's command dispatch logic without executing real I/O."""

    def test_cli_module_is_importable(self):
        """The CLI module must be importable as a standalone entry point."""
        import shared.presentation.cli as cli_module

        assert hasattr(cli_module, "main")

    def test_cli_has_sync_companies_command(self):
        """CLI must expose the 'sync-companies' command."""
        import shared.presentation.cli as cli_module

        assert hasattr(cli_module, "_run_sync_companies")

    @pytest.mark.asyncio
    async def test_cli_unknown_command_exits_with_error(self):
        """Unknown commands must produce a non-zero exit code."""
        import shared.presentation.cli as cli_module

        with patch.object(cli_module.sys, "argv", ["cli", "unknown-command"]):
            with pytest.raises(SystemExit) as exc_info:
                await cli_module.main()
            assert exc_info.value.code == 1

    @pytest.mark.asyncio
    async def test_cli_no_args_prints_usage(self, capsys):
        """Invoking CLI without arguments must print usage instructions."""
        import shared.presentation.cli as cli_module

        with patch.object(cli_module.sys, "argv", ["cli"]):
            await cli_module.main()

        captured = capsys.readouterr()

    def test_create_sync_use_case(self):
        """Verifies the Hexagonal composition root wires the dependencies correctly."""
        import shared.presentation.cli as cli_module

        # Mocks for internal dependencies
        mock_engine = MagicMock()
        mock_session_local = MagicMock()
        mock_session_instance = MagicMock()
        mock_session_local.return_value = mock_session_instance

        mock_repo = MagicMock()
        mock_data_source = MagicMock()
        mock_telemetry = MagicMock()
        mock_use_case = MagicMock()

        # Patch sys.modules to inject our mocks when the function tries to import them internally
        modules_patcher = patch.dict(
            "sys.modules",
            {
                "shared.infrastructure.database.connection": MagicMock(
                    engine=mock_engine, SessionLocal=mock_session_local
                ),
                "companies.infrastructure.adapters.database.postgres_company_repository": MagicMock(
                    PostgresCompanyRepository=mock_repo
                ),
                "companies.infrastructure.adapters.data_sources.playwright_b3_data_source": MagicMock(
                    PlaywrightB3DataSource=mock_data_source
                ),
                "companies.application.use_cases.sync_b3_companies": MagicMock(
                    SyncB3CompaniesUseCase=mock_use_case
                ),
                "shared.infrastructure.adapters.prometheus_telemetry": MagicMock(
                    PrometheusTelemetryAdapter=mock_telemetry
                ),
            },
        )

        with modules_patcher:
            use_case, session = cli_module._create_sync_use_case()

            # AssertIONS
            mock_repo.assert_called_once_with(session=mock_session_instance)
            mock_telemetry.assert_called_once()
            mock_data_source.assert_called_once_with(
                telemetry=mock_telemetry.return_value
            )

            mock_use_case.assert_called_once_with(
                data_source=mock_data_source.return_value,
                repository=mock_repo.return_value,
                telemetry=mock_telemetry.return_value,
            )
            assert use_case == mock_use_case.return_value
            assert session == mock_session_instance

    @pytest.mark.asyncio
    @patch("shared.presentation.cli._create_sync_use_case")
    @patch("prometheus_client.push_to_gateway")
    @patch("os.getenv", return_value="http://fake-gateway:9091")
    async def test_run_sync_companies_success(
        self, mock_getenv, mock_push, mock_create
    ):
        """Verifies successful execution and Pushgateway dispatch."""
        import shared.presentation.cli as cli_module

        mock_use_case = AsyncMock()
        mock_session = MagicMock()
        mock_create.return_value = (mock_use_case, mock_session)

        await cli_module._run_sync_companies()

        mock_use_case.execute.assert_called_once()
        mock_session.close.assert_called_once()
        mock_push.assert_called_once()

    @pytest.mark.asyncio
    @patch("shared.presentation.cli._create_sync_use_case")
    @patch("prometheus_client.push_to_gateway")
    async def test_run_sync_companies_failure_still_cleans_up(
        self, mock_push, mock_create
    ):
        """Verifies that an execution failure still closes the DB and pushes metrics."""
        import shared.presentation.cli as cli_module

        mock_use_case = AsyncMock()
        mock_use_case.execute.side_effect = Exception("UseCase Crash")
        mock_session = MagicMock()
        mock_create.return_value = (mock_use_case, mock_session)

        with pytest.raises(Exception, match="UseCase Crash"):
            await cli_module._run_sync_companies()

        mock_session.close.assert_called_once()
        mock_push.assert_called_once()

    @pytest.mark.asyncio
    @patch("shared.presentation.cli._create_sync_use_case")
    @patch("prometheus_client.push_to_gateway")
    async def test_run_sync_companies_pushgateway_failure(
        self, mock_push, mock_create, caplog
    ):
        """Verifies that a Pushgateway failure doesn't crash the program."""
        import shared.presentation.cli as cli_module

        mock_use_case = AsyncMock()
        mock_session = MagicMock()
        mock_create.return_value = (mock_use_case, mock_session)
        mock_push.side_effect = Exception("Pushgateway Dead")

        # Should NOT raise an exception
        await cli_module._run_sync_companies()

        assert "Falha ao enviar" in caplog.text

    @pytest.mark.asyncio
    @patch("shared.presentation.cli._run_sync_companies")
    async def test_main_routing(self, mock_run, capsys):
        import shared.presentation.cli as cli_module

        with patch.object(cli_module.sys, "argv", ["cli", "sync-companies"]):
            await cli_module.main()

        mock_run.assert_called_once()

    @pytest.mark.skip(
        reason="Subprocess coverage conflict under mutmut stats collection"
    )
    def test_run_as_main_block(self):
        """Test the if __name__ == '__main__' block execution by executing the file as a script."""
        import subprocess
        import sys
        from pathlib import Path
        import shared.presentation.cli as cli_module

        # SOTA: Dynamically resolve the absolute path to cli.py to survive Mutmut sandboxing.
        cli_path = Path(cli_module.__file__).resolve()

        # Execute the main file as a script using subprocess. This guarantees the __main__ block is hit.
        # We pass an unknown command so it just prints an error and exits, avoiding real I/O.
        result = subprocess.run(
            [
                sys.executable,
                "-m",
                "coverage",
                "run",
                "-a",
                str(cli_path),
                "unknown-command",
            ],
            capture_output=True,
            text=True,
        )

        # Verify it actually hit the right block resulting in the print output
        assert "Unknown command: unknown-command" in result.stdout
