import sys
from abc import ABC, abstractmethod

class AbstractClass(ABC):

    def template_method(self):
        self.__always_do_this()
        self.do_step_1()
        self.do_step_2()
        self.do_this_or()

    def __always_do_this(self):
        name = sys._getframe().f_code.co_name
        print(f'{self.__class__}-{name}')

    @abstractmethod
    def do_step_1(self):
        pass

    @abstractmethod
    def do_step_2(self):
        pass

    def do_this_or(self):
        print("You can overide me but you don't have to")


class ConcreteClassA(AbstractClass):

    def do_step_1(self):
        print('Doing step 1 for concrete class A')

    def do_step_2(self):
        print('Doing step 2 for concrete class A')


class ConcreteClassB(AbstractClass):

    def do_step_1(self):
        print('Doing step 1 for concrete class B')

    def do_step_2(self):
        print('Doing step 2 for concrete class B')

    def do_this_or(self):
        print('Doing my own business')


if __name__ == '__main__':

    a = ConcreteClassA()
    a.template_method()

    b = ConcreteClassB()
    b.template_method()
