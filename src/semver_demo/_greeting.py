def greet(name):
    """Return a greeting for name."""
    return f"Hello, {name}!"


class Greeter:
    """Greets people with a fixed punctuation mark."""

    def __init__(self, punctuation="!"):
        self.punctuation = punctuation

    def greet(self, name):
        """Return a greeting for name."""
        return f"Hello, {name}{self.punctuation}"
