# implicit inheritance
class Parent(object):

    def implicit(self):
        print("PARENT implicit()")


class Child(Parent):
    pass

dad = Parent()
son = Child()

dad.implicit()
son.implicit()  # will also call implicit()

""" if you put functions on base class (Parent), then
all subclasses (Child) will automatically get those
features"""

# override explicitly
""" because you want the child to behave differently"""


class Parent_2(object):

    def override(self):
        print("PARENT override()")


class Child_2(Parent_2):

    def override(self):
        print("CHILD override()")


dad_2 = Parent_2()
son_2 = Child_2()  # son is an instance of Child

dad_2.override()
son_2.override()

""" special case of overriding where you want to alter
the behavior before or after the Parent class's
version runs. FIRST, override the function, but
then use a Python built-in function super
to get to the Parent version to call."""


class Parent_3(object):

    def altered(self):
        print("PARENT altered()")

class Child_3(Parent_3):

    def altered(self):
        print("CHILD, BEFORE PARENT altered()")
        super(Child_3, self).altered()
        print("CHILD, AFTER PARENT altered()")


dad_3 = Parent_3()
son_3 = Child_3()

dad_3.altered()
son_3.altered()

"""
1. print("CHILD, BEFORE PARENT altered()")
Parent_3.altered is overridden so Child_3.altered
version runs.

2. use super to get Parent_3.altered version

3. super(Child, self).altered()
the code is aware of inheritance and will get the
Parent_3 class for you.

"call super with arguments Child_3 and self, then 
call the function altered on whatever it returns."

4. at this  point, Parent_3.altered version of the
function runs and print the message

5. finally, returns from Parent_3.altered 
to Child_3.altered and continues to print the message

print("CHILD, AFTER PARENT altered()")
"""
