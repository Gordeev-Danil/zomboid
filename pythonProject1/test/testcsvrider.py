import unittest
from zomboid import CSVRider


class TestCSVRider(unittest.TestCase):
    def setUp(self):
        self.zomboid = CSVRider("items.csv")

    def test_get_item_by_id(self):
        item = self.zomboid.get_item_by_id(1)
        self.assertIsNotNone(item)
        self.assertEqual(item.name, "Hummer")

    def test_search_items_by_name(self):
        results = self.zomboid.search_items_by_name("Nails")
        self.assertGreater(len(results), 0)

    def test_display_items_paginated(self):
        pass

if __name__ == "__main__":
    unittest.main()