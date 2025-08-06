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