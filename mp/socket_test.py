# Reference: https://docs.python.org/2/library/unittest.html
import unittest
from mp_socket import mp_socket

class mp_socket_test(unittest.TestCase):
    def test_setupServer(self):
        print("Test Setup Server")
        self.assertEqual(mp_socket().connection("test_setupServer"), True)

    def test_ConnectToServer(self):
        print("-------------------------")
        print("Test Connect to Server")
        self.assertEqual(mp_socket().connection("test_ConnectToServer"), True)

    # def test_isupper(self):
    #     self.assertTrue("FOO".isupper())
    #     self.assertFalse("Foo".isupper())

    # def test_split(self):
    #     s = "hello world"
    #     self.assertEqual(s.split(), ["hello", "world"])
        
    #     # Check that s.split fails when the separator is not a string.
    #     with self.assertRaises(TypeError):
    #         s.split(2)

if __name__ == "__main__":
    unittest.main()
