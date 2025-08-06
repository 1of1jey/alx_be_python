class Book:
    """Base class representing a book with title and author."""

    def __init__(self, title, author):
        """Initialize a book with title and author.

        Args:
            title (str): The title of the book
            author (str): The author of the book
        """
        self.title = title
        self.author = author

    def __str__(self):
        """Return string representation of the book."""
        return f"Book: {self.title} by {self.author}"

class EBook(Book):
        def __init__(self, title, author, file_size):
            super().__init__(title, author)  # Call parent class constructor
            self.file_size = file_size

        def __str__(self):
            return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)  # Call parent class constructor
        self.page_count = page_count

    def __str__(self):
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"

