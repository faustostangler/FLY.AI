import asyncio
import sys

async def main():
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

if __name__ == "__main__":
    asyncio.run(main())
