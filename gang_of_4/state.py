# base state class
class AtmState():

    name = 'state'
    allowed = []

    def go_next(self, state):
        if state.name in self.allowed:
            print(f'Current state: {self}, switched to: {state.name}')
            self.__class__ = state
        else:
            print(f'Current state: {self}, switching to: {state.name} not possible!')

    def __str__(self):
        return self.name

# concrete class
class off(AtmState):

    name = "off"
    allowed = ['on']


class On(AtmState):

    name = "on"
    allowed = ["off"]


class ATM():

    def __init__(self):
        self.current = off()

    def set_state(self, state):
        self.current.go_next(state)


if __name__ == '__main__':
    atm = ATM()
    atm.set_state(On)
    atm.set_state(off)
    atm.set_state(off)
    atm.set_state(On)
