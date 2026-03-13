import asyncio
import sys
from typing import Annotated
from typing import Callable
from typing import ClassVar

MutantDict = Annotated[dict[str, Callable], "Mutant"] # type: ignore


def _mutmut_trampoline(orig, mutants, call_args, call_kwargs, self_arg = None): # type: ignore
    """Forward call to original or mutated function, depending on the environment"""
    import os # type: ignore
    mutant_under_test = os.environ['MUTANT_UNDER_TEST'] # type: ignore
    if mutant_under_test == 'fail': # type: ignore
        from mutmut.__main__ import MutmutProgrammaticFailException # type: ignore
        raise MutmutProgrammaticFailException('Failed programmatically')       # type: ignore
    elif mutant_under_test == 'stats': # type: ignore
        from mutmut.__main__ import record_trampoline_hit # type: ignore
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__) # type: ignore
        # (for class methods, orig is bound and thus does not need the explicit self argument)
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_' # type: ignore
    if not mutant_under_test.startswith(prefix): # type: ignore
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    mutant_name = mutant_under_test.rpartition('.')[-1] # type: ignore
    if self_arg is not None: # type: ignore
        # call to a class method where self is not bound
        result = mutants[mutant_name](self_arg, *call_args, **call_kwargs) # type: ignore
    else:
        result = mutants[mutant_name](*call_args, **call_kwargs) # type: ignore
    return result # type: ignore

async def main():
    args = []# type: ignore
    kwargs = {}# type: ignore
    return await _mutmut_trampoline(x_main__mutmut_orig, x_main__mutmut_mutants, args, kwargs, None)

async def x_main__mutmut_orig():
    if len(sys.argv) < 2:
        print("Usage: python -m src.shared.presentation.cli [command]")
        return

    cmd = sys.argv[1]
    if cmd == "sync-companies":
        print("Starting Companies Sync (CLI Manifestation)...")
        # In a real app, instantiate the use case directly here
        # For now, just a placeholder to show the "Container as SSOT" pattern
        await asyncio.sleep(1)
        print("Sync Completed.")
    else:
        print(f"Unknown command: {cmd}")

async def x_main__mutmut_1():
    if len(sys.argv) <= 2:
        print("Usage: python -m src.shared.presentation.cli [command]")
        return

    cmd = sys.argv[1]
    if cmd == "sync-companies":
        print("Starting Companies Sync (CLI Manifestation)...")
        # In a real app, instantiate the use case directly here
        # For now, just a placeholder to show the "Container as SSOT" pattern
        await asyncio.sleep(1)
        print("Sync Completed.")
    else:
        print(f"Unknown command: {cmd}")

async def x_main__mutmut_2():
    if len(sys.argv) < 3:
        print("Usage: python -m src.shared.presentation.cli [command]")
        return

    cmd = sys.argv[1]
    if cmd == "sync-companies":
        print("Starting Companies Sync (CLI Manifestation)...")
        # In a real app, instantiate the use case directly here
        # For now, just a placeholder to show the "Container as SSOT" pattern
        await asyncio.sleep(1)
        print("Sync Completed.")
    else:
        print(f"Unknown command: {cmd}")

async def x_main__mutmut_3():
    if len(sys.argv) < 2:
        print(None)
        return

    cmd = sys.argv[1]
    if cmd == "sync-companies":
        print("Starting Companies Sync (CLI Manifestation)...")
        # In a real app, instantiate the use case directly here
        # For now, just a placeholder to show the "Container as SSOT" pattern
        await asyncio.sleep(1)
        print("Sync Completed.")
    else:
        print(f"Unknown command: {cmd}")

async def x_main__mutmut_4():
    if len(sys.argv) < 2:
        print("XXUsage: python -m src.shared.presentation.cli [command]XX")
        return

    cmd = sys.argv[1]
    if cmd == "sync-companies":
        print("Starting Companies Sync (CLI Manifestation)...")
        # In a real app, instantiate the use case directly here
        # For now, just a placeholder to show the "Container as SSOT" pattern
        await asyncio.sleep(1)
        print("Sync Completed.")
    else:
        print(f"Unknown command: {cmd}")

async def x_main__mutmut_5():
    if len(sys.argv) < 2:
        print("usage: python -m src.shared.presentation.cli [command]")
        return

    cmd = sys.argv[1]
    if cmd == "sync-companies":
        print("Starting Companies Sync (CLI Manifestation)...")
        # In a real app, instantiate the use case directly here
        # For now, just a placeholder to show the "Container as SSOT" pattern
        await asyncio.sleep(1)
        print("Sync Completed.")
    else:
        print(f"Unknown command: {cmd}")

async def x_main__mutmut_6():
    if len(sys.argv) < 2:
        print("USAGE: PYTHON -M SRC.SHARED.PRESENTATION.CLI [COMMAND]")
        return

    cmd = sys.argv[1]
    if cmd == "sync-companies":
        print("Starting Companies Sync (CLI Manifestation)...")
        # In a real app, instantiate the use case directly here
        # For now, just a placeholder to show the "Container as SSOT" pattern
        await asyncio.sleep(1)
        print("Sync Completed.")
    else:
        print(f"Unknown command: {cmd}")

async def x_main__mutmut_7():
    if len(sys.argv) < 2:
        print("Usage: python -m src.shared.presentation.cli [command]")
        return

    cmd = None
    if cmd == "sync-companies":
        print("Starting Companies Sync (CLI Manifestation)...")
        # In a real app, instantiate the use case directly here
        # For now, just a placeholder to show the "Container as SSOT" pattern
        await asyncio.sleep(1)
        print("Sync Completed.")
    else:
        print(f"Unknown command: {cmd}")

async def x_main__mutmut_8():
    if len(sys.argv) < 2:
        print("Usage: python -m src.shared.presentation.cli [command]")
        return

    cmd = sys.argv[2]
    if cmd == "sync-companies":
        print("Starting Companies Sync (CLI Manifestation)...")
        # In a real app, instantiate the use case directly here
        # For now, just a placeholder to show the "Container as SSOT" pattern
        await asyncio.sleep(1)
        print("Sync Completed.")
    else:
        print(f"Unknown command: {cmd}")

async def x_main__mutmut_9():
    if len(sys.argv) < 2:
        print("Usage: python -m src.shared.presentation.cli [command]")
        return

    cmd = sys.argv[1]
    if cmd != "sync-companies":
        print("Starting Companies Sync (CLI Manifestation)...")
        # In a real app, instantiate the use case directly here
        # For now, just a placeholder to show the "Container as SSOT" pattern
        await asyncio.sleep(1)
        print("Sync Completed.")
    else:
        print(f"Unknown command: {cmd}")

async def x_main__mutmut_10():
    if len(sys.argv) < 2:
        print("Usage: python -m src.shared.presentation.cli [command]")
        return

    cmd = sys.argv[1]
    if cmd == "XXsync-companiesXX":
        print("Starting Companies Sync (CLI Manifestation)...")
        # In a real app, instantiate the use case directly here
        # For now, just a placeholder to show the "Container as SSOT" pattern
        await asyncio.sleep(1)
        print("Sync Completed.")
    else:
        print(f"Unknown command: {cmd}")

async def x_main__mutmut_11():
    if len(sys.argv) < 2:
        print("Usage: python -m src.shared.presentation.cli [command]")
        return

    cmd = sys.argv[1]
    if cmd == "SYNC-COMPANIES":
        print("Starting Companies Sync (CLI Manifestation)...")
        # In a real app, instantiate the use case directly here
        # For now, just a placeholder to show the "Container as SSOT" pattern
        await asyncio.sleep(1)
        print("Sync Completed.")
    else:
        print(f"Unknown command: {cmd}")

async def x_main__mutmut_12():
    if len(sys.argv) < 2:
        print("Usage: python -m src.shared.presentation.cli [command]")
        return

    cmd = sys.argv[1]
    if cmd == "sync-companies":
        print(None)
        # In a real app, instantiate the use case directly here
        # For now, just a placeholder to show the "Container as SSOT" pattern
        await asyncio.sleep(1)
        print("Sync Completed.")
    else:
        print(f"Unknown command: {cmd}")

async def x_main__mutmut_13():
    if len(sys.argv) < 2:
        print("Usage: python -m src.shared.presentation.cli [command]")
        return

    cmd = sys.argv[1]
    if cmd == "sync-companies":
        print("XXStarting Companies Sync (CLI Manifestation)...XX")
        # In a real app, instantiate the use case directly here
        # For now, just a placeholder to show the "Container as SSOT" pattern
        await asyncio.sleep(1)
        print("Sync Completed.")
    else:
        print(f"Unknown command: {cmd}")

async def x_main__mutmut_14():
    if len(sys.argv) < 2:
        print("Usage: python -m src.shared.presentation.cli [command]")
        return

    cmd = sys.argv[1]
    if cmd == "sync-companies":
        print("starting companies sync (cli manifestation)...")
        # In a real app, instantiate the use case directly here
        # For now, just a placeholder to show the "Container as SSOT" pattern
        await asyncio.sleep(1)
        print("Sync Completed.")
    else:
        print(f"Unknown command: {cmd}")

async def x_main__mutmut_15():
    if len(sys.argv) < 2:
        print("Usage: python -m src.shared.presentation.cli [command]")
        return

    cmd = sys.argv[1]
    if cmd == "sync-companies":
        print("STARTING COMPANIES SYNC (CLI MANIFESTATION)...")
        # In a real app, instantiate the use case directly here
        # For now, just a placeholder to show the "Container as SSOT" pattern
        await asyncio.sleep(1)
        print("Sync Completed.")
    else:
        print(f"Unknown command: {cmd}")

async def x_main__mutmut_16():
    if len(sys.argv) < 2:
        print("Usage: python -m src.shared.presentation.cli [command]")
        return

    cmd = sys.argv[1]
    if cmd == "sync-companies":
        print("Starting Companies Sync (CLI Manifestation)...")
        # In a real app, instantiate the use case directly here
        # For now, just a placeholder to show the "Container as SSOT" pattern
        await asyncio.sleep(None)
        print("Sync Completed.")
    else:
        print(f"Unknown command: {cmd}")

async def x_main__mutmut_17():
    if len(sys.argv) < 2:
        print("Usage: python -m src.shared.presentation.cli [command]")
        return

    cmd = sys.argv[1]
    if cmd == "sync-companies":
        print("Starting Companies Sync (CLI Manifestation)...")
        # In a real app, instantiate the use case directly here
        # For now, just a placeholder to show the "Container as SSOT" pattern
        await asyncio.sleep(2)
        print("Sync Completed.")
    else:
        print(f"Unknown command: {cmd}")

async def x_main__mutmut_18():
    if len(sys.argv) < 2:
        print("Usage: python -m src.shared.presentation.cli [command]")
        return

    cmd = sys.argv[1]
    if cmd == "sync-companies":
        print("Starting Companies Sync (CLI Manifestation)...")
        # In a real app, instantiate the use case directly here
        # For now, just a placeholder to show the "Container as SSOT" pattern
        await asyncio.sleep(1)
        print(None)
    else:
        print(f"Unknown command: {cmd}")

async def x_main__mutmut_19():
    if len(sys.argv) < 2:
        print("Usage: python -m src.shared.presentation.cli [command]")
        return

    cmd = sys.argv[1]
    if cmd == "sync-companies":
        print("Starting Companies Sync (CLI Manifestation)...")
        # In a real app, instantiate the use case directly here
        # For now, just a placeholder to show the "Container as SSOT" pattern
        await asyncio.sleep(1)
        print("XXSync Completed.XX")
    else:
        print(f"Unknown command: {cmd}")

async def x_main__mutmut_20():
    if len(sys.argv) < 2:
        print("Usage: python -m src.shared.presentation.cli [command]")
        return

    cmd = sys.argv[1]
    if cmd == "sync-companies":
        print("Starting Companies Sync (CLI Manifestation)...")
        # In a real app, instantiate the use case directly here
        # For now, just a placeholder to show the "Container as SSOT" pattern
        await asyncio.sleep(1)
        print("sync completed.")
    else:
        print(f"Unknown command: {cmd}")

async def x_main__mutmut_21():
    if len(sys.argv) < 2:
        print("Usage: python -m src.shared.presentation.cli [command]")
        return

    cmd = sys.argv[1]
    if cmd == "sync-companies":
        print("Starting Companies Sync (CLI Manifestation)...")
        # In a real app, instantiate the use case directly here
        # For now, just a placeholder to show the "Container as SSOT" pattern
        await asyncio.sleep(1)
        print("SYNC COMPLETED.")
    else:
        print(f"Unknown command: {cmd}")

async def x_main__mutmut_22():
    if len(sys.argv) < 2:
        print("Usage: python -m src.shared.presentation.cli [command]")
        return

    cmd = sys.argv[1]
    if cmd == "sync-companies":
        print("Starting Companies Sync (CLI Manifestation)...")
        # In a real app, instantiate the use case directly here
        # For now, just a placeholder to show the "Container as SSOT" pattern
        await asyncio.sleep(1)
        print("Sync Completed.")
    else:
        print(None)

x_main__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_main__mutmut_1': x_main__mutmut_1, 
    'x_main__mutmut_2': x_main__mutmut_2, 
    'x_main__mutmut_3': x_main__mutmut_3, 
    'x_main__mutmut_4': x_main__mutmut_4, 
    'x_main__mutmut_5': x_main__mutmut_5, 
    'x_main__mutmut_6': x_main__mutmut_6, 
    'x_main__mutmut_7': x_main__mutmut_7, 
    'x_main__mutmut_8': x_main__mutmut_8, 
    'x_main__mutmut_9': x_main__mutmut_9, 
    'x_main__mutmut_10': x_main__mutmut_10, 
    'x_main__mutmut_11': x_main__mutmut_11, 
    'x_main__mutmut_12': x_main__mutmut_12, 
    'x_main__mutmut_13': x_main__mutmut_13, 
    'x_main__mutmut_14': x_main__mutmut_14, 
    'x_main__mutmut_15': x_main__mutmut_15, 
    'x_main__mutmut_16': x_main__mutmut_16, 
    'x_main__mutmut_17': x_main__mutmut_17, 
    'x_main__mutmut_18': x_main__mutmut_18, 
    'x_main__mutmut_19': x_main__mutmut_19, 
    'x_main__mutmut_20': x_main__mutmut_20, 
    'x_main__mutmut_21': x_main__mutmut_21, 
    'x_main__mutmut_22': x_main__mutmut_22
}
x_main__mutmut_orig.__name__ = 'x_main'

if __name__ == "__main__":
    asyncio.run(main())
