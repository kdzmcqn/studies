from abc import abstractmethod, ABC


class BMW(ABC):
    def __init__(self, model):
        self.model = model

    def start(self):
        print('vroom')

    # for abstraction
    @abstractmethod  # TODO should be implemented by child classes
    def drive(self):
        pass


class Lol(BMW):
    def __init__(self, model):
        super().__init__(model)
        self.model = model

    def drive(self):
        print('must have drive method kasi')


class threeSeries(BMW):
    def __init__(self, gps, model):
        super().__init__(model)
        self.gps = gps

    def display(self):
        print(self.gps)

    def start(self):
        super().start()
        super().start()
        print('3 series vroom')

    def drive(self):
        print('driving 3 series')

    def stop(self):
        pass


car = threeSeries(True, 'The BMW')
print(car.gps)
print(car.model)
car.start()
car.drive()

car2 = Lol('the lol car')
print(car2.model)
car2.start()
car2.drive()

# * Interfacing
# a class wuth all the methods as abstract methods


class Plane(ABC):
    def __init__(self, wings):
        self.wings = wings

    # class now becomes an interface
    @abstractmethod
    def fly(self):
        pass


class F15(Plane):
    def __init__(self, wings):
        super().__init__(wings)
        self.wings = wings

    def fly(self):
        super().fly()
        print('flying')


class B2(Plane):
    def __init__(self, wings):
        super().__init__()
        self.wings = wings

    def fly(self):
        super().fly()
        print('swoosh')


someplane = F15('garuda-5')
print(someplane.wings)
someplane.fly()
bomber = B2('broadsword')
print(bomber.wings)
