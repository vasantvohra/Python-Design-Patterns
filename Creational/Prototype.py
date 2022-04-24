import copy


class Prototype:
    def __init__(self):
        self._objects = {}

    def register_object(self, name, obj):
        """"""
        # store the object to be cloned into a dictionary
        self._objects[name] = obj

    def unregister_object(self, name):
        del self._objects[name]

    def clone(self, name, **kwargs):
        obj = copy.deepcopy(self._objects.get(name))
        obj.__dict__.update(kwargs)
        return obj


class Car:
    def __init__(self):
        self.name = "Sky Lark"
        self.color = "Red"
        self.options = "example"

    def __str__(self):
        return f'{self.name}, {self.color}, {self.options}'


if __name__ == '__main__':
    car = Car()
    prototype = Prototype()
    prototype.register_object(name='skylark', obj=car)
    cloned_car = prototype.clone('skylark', color='black')
    print(cloned_car)
