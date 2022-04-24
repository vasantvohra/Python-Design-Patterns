from functools import wraps

def make_blink(function):
    """Defines the decorator."""
    # This makes the decorator transparent in terms of name
    @wraps(function)
    def decorator():
        # Define the inner function
        return f"<blink>{function()}</blink>"
    return decorator

@make_blink
def hello():
    """Original function."""
    return "Hello World!"


if __name__ == '__main__':
    print(hello())
    print(hello.__name__)
    print(hello.__doc__)
    help(hello)