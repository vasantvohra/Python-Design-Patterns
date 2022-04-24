class Borg:
    """The Borg design pattern."""
    _shared_data = {}

    def __init__(self):
        # Make an attribute dictionary
        self.__dict__ = self._shared_data


class Singleton(Borg):
    """The singleton class."""
    def __init__(self, **kwargs):
        super(Singleton, self).__init__()
        self._shared_data.update(kwargs)

    def __str__(self):
        return str(self._shared_data)


if __name__ == '__main__':
    x = Singleton(HTML="Hyper Text Markup Language")
    print(id(x), x)
    y = Singleton(HTTP="Hyper Text Transfer Protocol")
    print(id(y), y)
    z = Singleton(SNMP="Simple Network Management Protocol")
    print(id(z), z)
