class Car:
    def __init__(self, name):
        self.name = name
        self.model = None
        self.tires = None
        self.engine = None

    def __str__(self):
        return f'{self.name}: {self.model} | {self.tires} | {self.engine}'


class Builder:
    """Abstract Builder"""
    def __init__(self):
        self.car = None

    def create_new_car(self):
        self.car = Car("Ford")

    def add_model(self):
        raise NotImplementedError

    def add_tires(self):
        raise NotImplementedError

    def add_engine(self):
        raise NotImplementedError


class SkyLarkBuilder(Builder):
    """Concrete Builder -> provides parts and tools to work on the car."""

    def add_model(self):
        self.car.model = "Sky Lark"

    def add_tires(self):
        self.car.tires = "Regular Tires"

    def add_engine(self):
        self.car.engine = "Turbo Engine"


class MustangBuilder(Builder):
    """Concrete Builder -> provides parts and tools to work on the car."""

    def add_model(self):
        self.car.model = "Mustang"

    def add_tires(self):
        self.car.tires = "Apollo winter Tires"

    def add_engine(self):
        self.car.engine = "V8 Engine"


class Director:
    """Director"""
    def __init__(self, builder):
        self._builder = builder

    def construct_car(self):
        self._builder.create_new_car()
        self._builder.add_model()
        self._builder.add_tires()
        self._builder.add_engine()

    def get_car(self):
        return self._builder.car


if __name__ == '__main__':
    builder = SkyLarkBuilder()
    director = Director(builder)
    director.construct_car()
    car = director.get_car()
    print(car)
    builder = MustangBuilder()
    director = Director(builder)
    director.construct_car()
    car = director.get_car()
    print(car)

