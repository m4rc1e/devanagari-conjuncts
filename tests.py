import sys
import unittest
import conjuncts


class TestCase(unittest.TestCase):
    def check_lxml_is_installed(self):
        if ('lxml' in sys.modules or 'lxml' in sys.modules):
            self.assert_(True, "lxml is loaded")
        else:
            self.fail()


if __name__ == "__main__":
    unittest.main()
