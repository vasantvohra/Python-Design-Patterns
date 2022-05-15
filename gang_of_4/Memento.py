import pickle

class Originator:

    def __init__(self):
        self._state = None

    def create_memento(self):
        print(vars(self))
        return pickle.dumps(vars(self))

    def set_memento(self, memento):
        previous_state = pickle.loads(memento)
        vars(self).clear()
        vars(self).update(previous_state)

if __name__ == '__main__':
    originator = Originator()
    print(vars(originator))
    momento = originator.create_memento()
    originator._state = True
    print(vars(originator))
    originator.set_memento(momento)
    print(vars(originator))