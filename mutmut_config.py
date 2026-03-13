import sys
import os

# SOTA Mutmut Configuration
# Ensure the ABSOLUTE path to src is in the path for mutation runs
# This bypasses the sandbox limitations of mutmut 3.x
src_path = "/home/stangler/Documents/Python/FLY.AI/src"
if src_path not in sys.path:
    sys.path.insert(0, src_path)

def pre_mutation(context):
    """Hooks for mutmut"""
    pass
