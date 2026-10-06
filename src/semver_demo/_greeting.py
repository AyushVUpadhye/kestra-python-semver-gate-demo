GREETINGS = {"en": "Hello", "fr": "Bonjour"}


def greet(name, language):
    """Return a greeting for name in language (en or fr)."""
    return f"{GREETINGS[language]}, {name}!"


class Greeter:
    """Greets people with a fixed punctuation mark."""

    def __init__(self, punctuation="!"):
        self.punctuation = punctuation

    def greet(self, name, language):
        """Return a greeting for name in language (en or fr)."""
        return f"{GREETINGS[language]}, {name}{self.punctuation}"


def farewell(name):
    """Return a farewell for name."""
    return f"Goodbye, {name}!"
