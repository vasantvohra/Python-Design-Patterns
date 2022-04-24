import time


class Producer:
    """Define the 'resource-intensive' object to instantiate!"""
    def produce(self):
        print("Producer is working hard!")

    def meet(self):
        print("Producer has time to meet you now!")


class Proxy:
    def __init__(self):
        self.occupied = False
        self.produced = None

    def produce(self):
        print("Artist checking if producer is available")
        if not self.occupied:
            self.producer = Producer()
            time.sleep(2)
            self.producer.meet()
        else:
            time.sleep(2)
            print("Producer is busy")


if __name__ == '__main__':
    p = Proxy()
    p.produce()
    p.occupied = True
    p.produce()