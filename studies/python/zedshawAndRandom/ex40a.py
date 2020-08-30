mystuff = {'apple': "I AM APPLES!"}
print(mystuff['apple'])  # key is 'apple'

# this is a module mystuff.py
def apple():
    print("I AM APPLES")

import mystuff
mystuff.apple()

def apple():
    print("I AM APPLES!")

# this is just a variable
tangerine = "Living reflection of a dream"

import mystuff
mystuff.apple()
print(mystuff.tangerine)

mystuff['apple']  # get apple from dict
mystuff.apple()  # get apple from module
mystuff.tangerine  # same thing, it's just a variable

# dict style
mystuff['apples']

# module style
mystuff.apples()

#  classes are like modules
class MyStuff(object):

    def __init__(self):
        self.tangerine = "And now a thousand years between"

    def apple(self):
        print("I AM CLASSY APPLES!")



# class style
thing = MyStuff()
thing.apples()
print(thing.tangerine)