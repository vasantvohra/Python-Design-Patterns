class SubsystemA:

    def method1(self):
        print('Subsystem A method 1 ...')

    def method2(self):
        print('Subsystem A method 2 ...')


class SubsystemB:

    def method1(self):
        print('Subsystem B method 1 ...')

    def method2(self):
        print('Subsystem B method 2 ...')


class Facade:

    def __init__(self):
        self._subsystem_A = SubsystemA()
        self._subsystem_B = SubsystemB()

    def method(self):
        self._subsystem_A.method1()
        self._subsystem_A.method2()
        self._subsystem_B.method1()
        self._subsystem_B.method2()


if __name__ == '__main__':
    facade = Facade()
    facade.method()