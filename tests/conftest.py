import sys
import os

# SOTA Architecture: Ensure src is in the path for all tests and tools
# conftest.py is in tests/, so src is at ../src
src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src"))
if src_path not in sys.path:
    sys.path.insert(0, src_path)
