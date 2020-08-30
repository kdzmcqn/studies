
# * Duck-Typing
class Duck:
    def talk(self):
        print("Quack")


class Human:
    def talk(self):
        print("Hello")


def callTalk(obj):
    obj.talk()


d = Duck()
callTalk(d)

h = Human()
callTalk(h)


# * Dependency Injection
class Flight:
    def __init__(self, engine):
        self.engine = engine

    def startEngine(self):
        self.engine.start()


class AirbusEngine:
    def start(self):
        print('starting airbus engine')


class BoeingEngine:
    def start(self):
        print('starting airbus engine')


oe = AirbusEngine()
f = Flight(oe)
f.startEngine()

be = BoeingEngine()
d = Flight(be)
d.startEngine()

# * Operator Overloading
x = 10
y = 20
print(x+y)
s1 = "Hello"
s2 = "Andro"
print(s1+s2)
l1 = [1, 2, 3]
l2 = [6, 5, 4]  # [1, 2, 3, 6, 5, 4]
print(l1+l2)

# * Runtime Polymorphism
# * Method Overriding


class BMW:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year


class ThreeSeries(BMW):

    def __init__(self, cruisControlEnabled, make, model, year):
        BMW.__init__(self, make, model, year)
        self.cruisControlEnabled = cruisControlEnabled


class FiveSeries(BMW):

    def __init__(self, parkingAssistEnabled, make, model, year):
        BMW.__init__(self, make, model, year)
        self.parkingAssistEnabled = parkingAssistEnabled


# * this is where method overloading happens
bmw = ThreeSeries(True, 'BMW', '328i', '2018')
print(bmw.cruisControlEnabled)
'''
In Java, we specify the type
BMW  bmw = ThreeSeries(True, 'BMW', '328i', '2018')
'''
# EOF
