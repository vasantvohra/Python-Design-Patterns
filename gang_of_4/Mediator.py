class Colleague(object):
    def __init__(self, mediator, id):
        self._mediator = mediator
        self._id = id

    def get_id(self):
        return self._id

    def send(self, message):
        pass

    def receive(self, message):
        pass


class ConcreteColleague(Colleague):
    def __init__(self, mediator, id):
        super(ConcreteColleague, self).__init__(mediator, id)

    def send(self, message):
        print(f'Message "{message}" sent by a colleague, {self._id}')

    def receive(self, message):
        print(f'Message "{message}" received by a colleague, {self._id}')


class Mediator:

    def add(self, colleague):
        pass

    def distribute(self, sender, message):
        pass


class ConcreteMediator(Mediator):
    def __init__(self):
        super(ConcreteMediator, self).__init__()
        self._colleague = []

    def add(self, colleague):
        self._colleague.append(colleague)

    def distribute(self, sender, message):
        for colleague in self._colleague:
            if colleague.get_id() != sender.get_id():
                colleague.receive(message)


if __name__ == '__main__':
    mediator = ConcreteMediator()
    c1 = ConcreteColleague(mediator, 1)
    c2 = ConcreteColleague(mediator, 2)
    c3 = ConcreteColleague(mediator, 3)

    mediator.add(c1)
    mediator.add(c2)
    mediator.add(c3)
    message = "Hello Good morning"
    c1.send(message)
    mediator.distribute(c1, message)
    message = "Hi morning"
    c3.send(message)
    mediator.distribute(c3, message)
