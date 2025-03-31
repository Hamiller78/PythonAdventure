#from .module1 import Class1, function1
#from .module2 import Class2

# Import specific modules or classes to make them available at the package level
from .Room import Room  # Import Room class to make it available at the package level

# Define package-level variables or metadata
__version__ = "0.0.1"
__author__ = "Torben Kneesch"

# Optionally, define what gets imported with `from World import *`
__all__ = ["Room", "Player"]