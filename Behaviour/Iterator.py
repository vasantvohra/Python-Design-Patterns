
def count_to(count):
    """Our iterator implementation"""
    # Our list
    numbers_in_german = ["eins", "zwei", "drei", "vier", "funf"]

    # Our built-in iterator
    # Creates a tuple such as (1, "eins")
    iterator = zip(range(count), numbers_in_german)

    # Iterate through our iterable list
    # Extract the German numbers
    # Put them in a generator called number
    for position, number in iterator:
        # Returns a 'generator' containing numbers in German
        yield number


if __name__ == '__main__':
    # Let's test the generator returned by our iterator
    for num in count_to(3):
        print("{}".format(num))
    print('Till 9')
    for num in count_to(9):
        print("{}".format(num))

    # Now manually
    num = count_to(5)
    print("Now manually")
    # step 1
    print(next(num))
    # step 2
    print(next(num))