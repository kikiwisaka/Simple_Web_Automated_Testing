# TODO
# Create Function to import lib
# Create Function to load the function
# Create Function to execute the function

import importlib

class Call:
    def __init__(self):
        pass

    @staticmethod
    def module(module_name: str, package_name: str=None):
        try:
            m = importlib.import_module(module_name, package_name)
            return m
        except ImportError as e:
            print(e)
        except ValueError as e:
            print(e)

    @staticmethod
    def function():
        pass

# x = Call.module('.login', 'Android.modules')