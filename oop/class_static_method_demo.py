class Calculator:
    """Calculator class demonstrating class methods and static methods."""

    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """Add two numbers using a static method.

        Static methods don't have access to class or instance attributes.
        They behave like regular functions but belong to the class namespace.

        Args:
            a (int or float): First number to add.
            b (int or float): Second number to add.

        Returns:
            int or float: The sum of a and b.
        """
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """Multiply two numbers using a class method.

        Class methods have access to class attributes via the 'cls' parameter.
        They can access and modify class-level data.


        print(f"Calculation type: {cls.calculation_type}")
        return a * b