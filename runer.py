import unittest

# Discover and run tests
if __name__ == "__main__":
    loader = unittest.TestLoader()
    suite = loader.discover(start_dir="tests", pattern="test_amazon.py")

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
