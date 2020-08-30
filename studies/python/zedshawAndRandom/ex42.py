## animal is-a object (yes, sort of confusing)
class Animal(object):
        pass

## dog is-a animal
class Dog(Animal):

    def __init__(self, name):
        ## dog has-a name
        self.name = name

## cat is-a animal
class Cat(Animal):

    def __init__(self, name):
        ## cat has-a name
        self.name = name

## person is-a object
class Person(object):

    def __init__(self, name):
        ## person has-a name
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None  # to make sure that the default is None

## employee is-a person
class Employee(Person):

    def __init__(self, name, salary):
        ## employee has-a name and salary
        super(Employee, self).__init__(name)
        ## employee has-a salary
        self.salary = salary


## fish is-a object
class Fish(object):
    pass

## salmon is-a fish
class Salmon(Fish):
    pass

## Halibut is-a fish
class Halibut(Fish):
    pass

## rover is-a Dog
rover = Dog("Rover")

## satan is-a cat
satan = Cat("Satan")

## mary is-a person
mary = Person("Mary")

## mary has-a pet satan
mary.pet = satan

## frank is-a employee has-a salary 120000
frank = Employee("Frank", 120000)

## frank has-a pet rover
frank.pet = rover


## flipper is-a fish
flipper = Fish()

## crouse is-a salmon
crouse = Salmon()

## harry is-a halibut
harry = Halibut()
