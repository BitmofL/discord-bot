import importlib
import sys

print('[startup_check] python:', sys.version)

try:
    disnake = importlib.import_module('disnake')
    print('[startup_check] disnake imported:', getattr(disnake, '__version__', 'unknown'))
except Exception as e:
    print('[startup_check] disnake import failed:', repr(e))
    raise

