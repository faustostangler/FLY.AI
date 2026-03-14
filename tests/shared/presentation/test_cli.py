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
        assert "Usage:" in captured.out
        assert "sync-companies" in captured.out
