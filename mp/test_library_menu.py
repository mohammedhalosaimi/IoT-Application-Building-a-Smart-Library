from library_menu import library_menu
import unittest

class TestBorrowReturn(unittest.TestCase):
    def setUp(self):
        self.user="Brad"
        self.menu=library_menu(self.user)
    def testBorrow(self):
        result=self.menu.borrowBook(self.user)
        self.assertTrue(result,True)
    
    def testReturn(self):
        result=self.menu.returnBook(self.user)
        self.assertTrue(result,True)
        
if __name__ == "__main__":
    unittest.main()

