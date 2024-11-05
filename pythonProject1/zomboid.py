import csv


class Item:
    def __init__(self, id, name, type, condition, amount):
        self.id = id
        self.name = name
        self.type = type
        self.condition = condition
        self.amount = amount

    def __str__(self):
        return f"{self.id} {self.name} {self.type} {self.condition} {self.amount}"


class CSVRider:
    def __init__(self, file_path):
        self.file_path = file_path
        self.items = self._load_items()

    def _load_items(self):
        items = []
        with open(self.file_path) as file:
            reader = csv.DictReader(file)
            for row in reader:
                item = Item(
                    id=int(row["ID"]),
                    name=row["Name"],
                    type=row["Type"],
                    condition=row["Condition"],
                    amount=int(row["Amount"])
                )
                items.append(item)
        return items

    def get_item_by_id(self, item_id):
        for item in self.items:
            if item.id == item_id:
                return item
        return None

    def search_items_by_name(self, name):
        return [item for item in self.items if name in item.name]

    def display_items_paginated(self, page_size=10):
        paginator = Paginator(self.items, page_size)
        for page in paginator:
            for item in page:
                print(item)
            input("Press Enter to view the next page...")


class Paginator:
    def __init__(self, items, page_size):
        self.items = items
        self.page_size = page_size
        self.current_page = 0

    def __iter__(self):
        self.current_page = 0
        return self

    def __next__(self):
        start = self.current_page * self.page_size
        end = start + self.page_size
        if start >= len(self.items):
            raise StopIteration
        self.current_page += 1
        return self.items[start:end]

if __name__ == "__main__":
    i = CSVRider("items.csv")
    #i.display_items_paginated(page_size=5)
    print(i.get_item_by_id(3))
    results = i.search_items_by_name("Nails")
    for item in results:
        print(item)