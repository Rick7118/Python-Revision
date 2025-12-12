# modules_and_imports_demo.py
# ---------------------------------------
# Modules & Imports — Self-documenting Python file
#
# This file contains explanatory comments and runnable examples
# that demonstrate how Python modules and imports work.
#
# Save this file and run parts of it, or import it from another file
# to see how import behavior differs from running directly.
# ---------------------------------------

# SECTION 1 — What is a module?
# A module is any .py file. Anything defined (variables, functions,
# classes) in a file can be imported by other files as a module.
#
# For example, if you save this file as modules_and_imports_demo.py,
# you can import it from another script with:
#
#    import modules_and_imports_demo
#
# or:
#
#    from modules_and_imports_demo import demo_function
#
# The module provides namespaced access: module.name

# A small value defined at module level:
MODULE_LEVEL_CONSTANT = "I am defined at module level"

# A helper function that demonstrates a callable inside a module.
def demo_function(name: str = "friend") -> str:
    """
    Simple function to demonstrate importing functions from modules.

    Returns a greeting string.
    """
    return f"Hello, {name}! (from demo_function)"


# SECTION 2 — import module (full module import)
# When you `import module_name`, Python executes the module file once
# (the first time it is imported) and binds the module object to the name.
#
# Use pattern:
#    import module_name
# then access names with:
#    module_name.some_function()
#
# Example usage (run in another script or interactive REPL):
#    import modules_and_imports_demo
#    print(modules_and_imports_demo.MODULE_LEVEL_CONSTANT)
#    print(modules_and_imports_demo.demo_function("Subhayu"))

# SECTION 3 — from module import name
# This imports a specific name from a module into the current namespace.
# Use when you want to reference the name directly without module prefix.
#
# Example:
#    from modules_and_imports_demo import demo_function
#    print(demo_function("Subhayu"))
#
# Be careful not to overwrite local names accidentally.

# SECTION 4 — aliasing imports
# You can shorten module names with `as`:
#
#    import modules_and_imports_demo as mid
#    print(mid.demo_function("Subhayu"))
#
# This is common for large libraries:
#    import numpy as np
#    import pandas as pd

# SECTION 5 — __name__ and script vs import behavior
# Every module has a special attribute __name__. When a module is run
# directly (python filename.py), __name__ == "__main__". When imported,
# __name__ is the module's filename (without .py).
#
# This idiom allows a file to expose functions for import while also
# providing a runnable demo when executed directly.
#
# Example pattern (used at the bottom of this file):

def _demo_print():
    """Small internal demo: prints the module constant and function output."""
    print(">>> Running demo from modules_and_imports_demo.py")
    print("MODULE_LEVEL_CONSTANT:", MODULE_LEVEL_CONSTANT)
    print("demo_function('You') ->", demo_function("You"))
    print()

# SECTION 6 — creating your own module files (folder structure)
# A module can be any .py file. A package is a folder containing modules
# and an __init__.py file. Example package layout:
#
# project/
#   app.py                 # top-level script
#   mypackage/
#       __init__.py        # package initializer
#       tools.py           # module: mypackage.tools
#       helpers.py         # module: mypackage.helpers
#
# Importing examples:
#   import mypackage.tools        # use mypackage.tools.func()
#   from mypackage import tools   # same as above
#   from mypackage.tools import some_func
#
# Note: modern Python doesn't require __init__.py in all cases (PEP 420
# namespace packages), but creating one is explicit and common.

# SECTION 7 — relative imports (inside packages)
# Within a package you can import sibling modules using relative imports:
#
# In mypackage/tools.py:
#    from .helpers import helper_func   # single dot = current package
#
# In mypackage/subpkg/mod.py:
#    from ..tools import some_tool      # two dots = parent package
#
# Relative imports only work when the package is imported, not when you run
# the module directly as a script (unless you adjust PYTHONPATH or use -m).

# SECTION 8 — import mechanics (brief overview)
# Python finds modules using sys.path (a list of directories). Key points:
#  - The directory containing the input script (or the current directory)
#    is included in sys.path.
#  - Site-packages (where pip installs packages) are included too.
#  - You can inspect sys.path:
#       import sys
#       print(sys.path)
#
# Avoid manipulating sys.path unless necessary. Use virtual environments
# and proper package installation (pip install -e .) for projects.

# SECTION 9 — from module import * (why to avoid)
# Do NOT use `from module import *` in production code.
# It imports all public names into your namespace and can cause name collisions.
# It is okay for quick interactive work or controlled __all__ exports, but generally
# avoid it in scripts and libraries.

# SECTION 10 — circular imports (common pitfall)
# Circular imports happen when module A imports module B and module B imports A.
# This causes partially-initialized modules and import errors.
#
# Example bad pattern:
#   # a.py
#   import b
#   def f(): ...
#
#   # b.py
#   import a
#   def g(): a.f()
#
# Fixes:
#  - Restructure code to avoid circular dependency (better)
#  - Move imports inside functions (lazy import)
#  - Create a third module that holds shared code used by both

# Example: lazy import to avoid circular import or heavy startup cost
def lazy_example():
    # Imagine we only sometimes need json; import it inside the function.
    import json
    return json.dumps({"lazy": True})

# SECTION 11 — best practices & style tips
# 1. Keep module responsibilities narrow ("single responsibility").
# 2. Use clear module names (avoid generic names like utils.py for big projects).
# 3. Avoid `from module import *`. Explicit is better.
# 4. Use aliases for well-known libraries (np, pd).
# 5. Put imports at the top of the file, except for lazy imports or when avoiding cycles.
# 6. Use __all__ if you want to control what `from module import *` exports:
#
#    __all__ = ["public_func", "PublicClass"]
#
# 7. Prefer functions and small modules; large classes and many responsibilities indicate
#    you should split the module.

# SECTION 12 — packaging and installing local modules
# For projects, you often want to install your package in "editable" mode:
# Create setup.cfg or pyproject.toml and run:
#    pip install -e .
#
# This makes the package importable from anywhere in your environment during development.

# SECTION 13 — demonstration of key import styles
# We'll create small helper names here to show how names would be bound when imported.

def add(a, b):
    """Simple add for demonstration"""
    return a + b

def multiply(a, b):
    """Simple multiply for demonstration"""
    return a * b

# Demonstration of __all__: controls wildcard import behavior.
# If someone does: from modules_and_imports_demo import *
# only the names listed in __all__ will be imported.
# If __all__ is not defined, Python will import all names that don't start with an underscore.
__all__ = ["demo_function", "add", "multiply", "MODULE_LEVEL_CONSTANT"]

# SECTION 14 — showing differences when importing vs running
# If you import this file as a module, the code at top-level executes once.
# If you run it as a script (python modules_and_imports_demo.py), we can run a demo.
# Use the guard below to run demo code only when executed directly (not on import).

if __name__ == "__main__":
    # This block runs when the file is executed directly.
    # It is a safe place for short demonstrations, tests, or CLI behavior.
    _demo_print()

    # Demonstrate lazy import usage
    print("lazy_example() ->", lazy_example())

    # Show that our simple functions work
    print("add(2,3) ->", add(2, 3))
    print("multiply(4,5) ->", multiply(4, 5))
    print()

    # Demonstrate usage that mimics import styles (commented guidance)
    print("Usage examples (run these in another file or interactive shell):")
    print("  import modules_and_imports_demo")
    print("  from modules_and_imports_demo import demo_function, add")
    print("  import modules_and_imports_demo as mid")
    print()

    # Demonstrate reading sys.path (only for interactive curiosity)
    import sys
    print("sys.path (first 5 entries):")
    for p in sys.path[:5]:
        print("  ", p)

# END OF FILE
