import unittest
from zomboid import Paginator
from zomboid import Item

class TestPaginator(unittest.TestCase):
    def setUp(self):
        items = [Item(i, f"Item {i}", "Type", "Good", i * 10) for i in range(30)]
        self.paginator = Paginator(items, 10)

    def test_pagination(self):
        pages = list(self.paginator)
        self.assertEqual(len(pages), 3)
        self.assertEqual(len(pages[0]), 10)
        self.assertEqual(pages[0][0].name, "Item 0")


if __name__ == "__main__":
    unittest.main()