class Korean:

    def __init__(self):
        self.name = "Korean"

    def speak_korean(self):
        return "An-neyong?"


class British:
    def __init__(self):
        self.name = "British"

    def speak_english(self):
        return "Hello"


class Adapter:

    def __init__(self, obj, **adapted_method):
        """Change the name of the method
        adapted_method - dictionary
        """
        self._object = obj
        # Add a new dictionary item that establishes the item
        self.__dict__.update(adapted_method)

    def __getattr__(self, attr):
        return getattr(self._object, attr)

    def __str__(self):
        return self.name


if __name__ == '__main__':
    objects = []
    korean = Korean()
    british = British()
    # append the Adapter objects with generic method
    objects.append(Adapter(korean, speak=korean.speak_korean))
    objects.append(Adapter(british, speak=british.speak_english))
    for obj in objects:
        print(f'{obj} says "{obj.speak()}"', end='\n')