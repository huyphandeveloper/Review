from abc import ABC, abstractmethod

class LibraryItem(ABC):
    def __init__(self, title, item_id):
        self.title = title
        self._item_id = item_id

    @property
    def item_id(self):
        return self._item_id

    @abstractmethod
    def get_info(self):
        pass

class Book(LibraryItem):
    def __init__(self, title, item_id, author):
        super().__init__(title, item_id)
        self.author = author

    def get_info(self):
        return f"[{self.item_id}] {self.title} by {self.author}"

class Magazine(LibraryItem):        
    def __init__(self, title, item_id, issue_number):
        super().__init__(title, item_id)
        self.issue_number = issue_number

    def get_info(self):
        return f"[{self.item_id}] {self.title} - Issue #{self.issue_number}"

def save_catalog(items : list, filename):
    with open(filename, "w") as f:
        for item in items:
            f.write(f"{item.get_info()}\n")

def load_catalog(filename):
    try:
        with open(filename, "r") as f:
            for line in f:
                print(line.strip())
    except FileNotFoundError:
        print("Catalog file not found")
        return None

items = [
    Book("Clean Code", "B001", "Robert Martin"),
    Magazine("National Geographic", "M001", 245)
]
save_catalog(items, "catalog.txt")
load_catalog("catalog.txt")
load_catalog("missing.txt")

lib_item = LibraryItem("Test", "X001")  # phải raise TypeError