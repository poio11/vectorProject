import unittest

if __name__ == "__main__":
    '''
    This run all of you tests at once.
    '''
    loader = unittest.TestLoader()
    suite = loader.discover("./tests", pattern="test_*.py")
    unittest.TextTestRunner().run(suite)
