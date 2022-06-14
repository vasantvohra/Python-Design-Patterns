
class Subject(object):
    """Represents what is being 'observed'"""
    def __init__(self):
        # This is where reference to all the observers are being kept
        # Note that this is a one-to-many relationship:
        # There will be one subject being observed by multiple observers.
        self._observers = set()

    def attach(self, observer):
        self._observers.add(observer)

    def detach(self, observer):
        if observer in self._observers:
            self._observers.remove(observer)

    def notify(self, modifier=None):
        for observer in self._observers:
            # Prevent notifying the observer that is actually updating the temperature.
            if modifier != observer:
                observer.update(self)

class Core(Subject):
    """Inherits from the Subject class"""
    def __init__(self, name=""):
        Subject.__init__(self)
        # Set the name of the core
        self._name = name
        # Initialize the temperature of the core
        self._temp = 0

    @property
    def temp(self):
        return self._temp

    @temp.setter
    def temp(self, temp):
        self._temp = temp
        # Notify the observers whenever somebody changes the core temperature
        self.notify()


class TempViewer:
    # Alert method that is invoked when the notify() method in a concrete subject is involved
    def update(self, subject):
        print("Temperature Viewer: {} has temperature {}".format(subject._name, subject._temp))


