# test code by this command --> python -m unittest test_greeter.py
# unittest test_greeter.py

import unittest
from greeter import Greeter

class TestGreeter(unittest.TestCase):
    def test_say_hello(self):
        g = Greeter("Siddharth")
        self.assertEqual(g.say_hello(), "Hello, Siddharth")
        
if __name__ == "__main__":
    unittest.main()