# book_class.py

class Book:
    def __init__(self, title, author, year):
        """Constructor that initializes title, author, and year"""
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """Destructor that prints when a Book object is deleted"""
        print(f"Deleting {self.title}")

    def __str__(self):
        """User-friendly string representation"""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Official string representation that can recreate the object"""
        return f"Book('{self.title}', '{self.author}', {self.year})"
