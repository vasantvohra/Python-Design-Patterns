
class House(object): # The class being visited
    def accept(self, visitor):
        """Interface to accept the visitor"""
        visitor.visit(self)

    def work_on_hvac(self, hvac_specialist):
        print(self, 'worked on by', hvac_specialist)

    def work_on_electricity(self, electrician):
        print(self, 'worked on by', electrician)

    def __str__(self):
        """Simply return the class name when the House object is printed."""
        return self.__class__.__name__


class Visitor(object):
    """Abstract visitor"""
    def __str__(self):
        """Simply return the class name when the Visitor object is printed."""
        return self.__class__.__name__


class HvacSpecialist(Visitor): # Inherits from the parent class,
    def visit(self, house):
        house.work_on_hvac(self)


class Electrician(Visitor):
    def visit(self, house):
        house.work_on_electricity(self)


if __name__ == '__main__':
    hv = HvacSpecialist()
    e = Electrician()
    home = House()
    home.accept(hv)
    home.accept(e)
