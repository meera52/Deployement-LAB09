import unittest
from book_manager import Book, BookManager

class TestBookManager(unittest.TestCase):
    def setUp(self):
        self.manager = BookManager()
        self.book1 = Book("1234567890", "Python Programming", "John Smith")
        self.book2 = Book("9876543210", "Data Science Handbook", "Alice Johnson")
        self.manager.add_book(self.book1)

    def test_add_book(self):
        self.manager.add_book(self.book2)
        self.assertEqual(len(self.manager.books), 2)
        self.assertIn(self.book2, self.manager.books)

    def test_add_duplicate_book(self):
        self.manager.add_book(self.book1)
        self.assertEqual(len(self.manager.books), 1)  # Ensure only one copy is added

    def test_remove_book(self):
        self.manager.remove_book("1234567890")
        self.assertEqual(len(self.manager.books), 0)
        self.assertNotIn(self.book1, self.manager.books)

    def test_remove_nonexistent_book(self):
        self.manager.remove_book("9999999999")  # ISBN that doesn't exist
        self.assertEqual(len(self.manager.books), 1)  # No change expected

    def test_list_books(self):
        books = self.manager.list_books()
        self.assertEqual(len(books), 1)
        self.assertIn(self.book1, books)

if __name__ == '__main__':
    unittest.main()
