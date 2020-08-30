"""

def hello():
    class Hi:  # metaclass define how this is created
        pass

    return Hi

# class define the rules of an object
# metaclass define the rules of a class


# class Test:
#     pass

print('-' * 10)

print(Test)  # prints <class '__main__.Test'>
print(Test())  # prints <__main__.Test object at 0x0000019D4B892EB8>

print('-' * 10)

print(type(Test()))  # <class '__main__.Test'> is possible cuz this class is an object
print(type(Test))  # <class 'type'>

print('-' * 10)


def func():
    pass


print(type(func))  # <class 'function'> cuz this function in an object
"""
"""
print('-' * 10)
print('-' * 10)

# we can make a class by doing this...


class Foo:
    def show(self):  # 'static', i.e. callable without having created a class instance before.
        print("hi")  # the warning happens on a member function that doesn't use self.
# simply use this # noinspection PyMethodMayBeStatic


def add_attribute(self):
    self.z = 9


Test = type('Test', (Foo,), {"x": 5, "add_attribute": add_attribute})  # equal to lines 11-12

# put comma to make sure it is registered as tuple (Foo,)

# type('A NAME', BASIS, ATTRIBUTE)
# name = internal representation of a class
# basis = anything we inherit from such as superclass or parent class
# attributes
t = Test()
t.wy = "hello"
print(t.wy)
print(t.x)
t.show()
t.add_attribute()
print(t.z)
"""


class Meta(type):
    def __new__(self, class_name, bases, attrs):  # before the init method; always called first
        print(attrs)

        a = {}
        for name, value in attrs.items():
            if name.startswith("__"):
                a[name] = value
            else:
                a[name.upper()] = value
        print(a)
        return type(class_name, bases, a)  # change attrs to a, vice-versa


class Dog(metaclass = Meta):
    x = 5
    y = 8

    def hello(self):
        print('hi')

d = Dog()
d.HELLO()