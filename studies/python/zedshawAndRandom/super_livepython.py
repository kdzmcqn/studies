class Base:
    def __init__(self):
        print('Base.__init__')

class Child1(Base):
    def __init__(self):
        super().__init__()
        print('Child1.__init__')

class Child2(Base):
    def __init__(self):
        super().__init__()
        print('Child2.__init__')

class Child3(Child1, Child2):
    def __init__(self):
        super().__init__()
        print('Child3.__init__')

c3 = Child3()
print(Child3.__mro__)  # mro - method resolution order
"""
>c3 = Child3()
output IF we use this line Base.__init__(self)

Base.__init__
Child1.__init__
Base.__init__
Child2.__init__
Child3.__init__
"""

class Ten:
    def adder(self, *args):
        print(sum(args) + 10)
        super().adder()  # will also call class 100

class Hundred:  # only connection is Experiment class inherits from both class
    def adder(self, *args):
        print(sum(args) + 100)

class Experiment(Ten, Hundred):  # class Ten is able to call class Hundred adder
    pass

print('-' * 20)
e = Experiment()
e.adder(1, 2, 3, 4)
print(Experiment.__mro__)  # super may invoke method a method we aren't expecting

"""
output w/ super():

20
100  class Hundred is called even no arguments to its adder passed
"""

"""
WITHOUT super()

class ChildB(Base):
    def __init__(self):
        mro = type(self).mro()             # Get the Method Resolution Order.
        check_next = mro.index(ChildB) + 1 # Start looking after *this* class.
        while check_next < len(mro):
            next_class = mro[check_next]
            if '__init__' in next_class.__dict__:
                next_class.__init__(self)
                break
            check_next += 1
Written a little more like native Python:

class ChildB(Base):
    def __init__(self):
        mro = type(self).mro()
        for next_class in mro[mro.index(ChildB) + 1:]: # slice to end
            if hasattr(next_class, '__init__'):
                next_class.__init__(self)
                break
                
"""