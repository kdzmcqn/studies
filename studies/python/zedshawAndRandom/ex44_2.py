# using super() with __init__
""" most common use is in __init__ functions in base
classes."""

# class Child(Parent):
#     def __init__(self, stuff):
#         self.stuff = stuff
#         super(Child, self).__init__()

# Composition
"""another way to do inheritance is to just use 
other classes and modules rather than rely on on
implicit inheritance"""

class Other(object):

    def override(self):
        print("OTHER override()")

    def implicit(self):
        print("OTHER implicit()")

    def altered(self):
        print("OTHER altered()")


class Child(object):

    def __init__(self):
        self.other = Other()

    def implicit(self):
        self.other.implicit()

    def override(self):
        print("CHILD override()")

    def altered(self):
        print("CHILD, BEFORE OTHER altered()")
        self.other.altered()
        print("CHILD, AFTER OTHER altered()")

son = Child()

son.implicit()
son.override()
son.altered()

"""almost the same as impilict inheritance
but you had to define Child.implicit function to do 
that one action

do we need other to be a class? or make another module
named other.py?"""

