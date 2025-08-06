class Book:
    def __init__(self, title, author, year):
        """Initialize a Book instance with title, author, and year."""
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """Destructor that prints a message when the book object is deleted."""
        print(f"Deleting {self.title}")

    def __str__(self):
        """Return informal string representation of the book."""
        return f"{self.title} by {self.author}, published in {self.year}"