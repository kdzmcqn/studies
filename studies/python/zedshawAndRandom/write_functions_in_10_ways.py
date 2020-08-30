def do_da_math(*numba):  # 1
    ex, way, zee = numba  # Dapat ganito. Bawal yung numba = ex, way, zee
    print(f"the x: {ex}, the y: {way}, the z: {zee}", end="\n")


# always to or more spaces after the functions (kahit pala comments...)
""" and comments is to whitespace after the lines"""


def do_mor_math(augend, addend):  # 2
    summer = augend + addend
    print(summer, end="\n")


def do_subtracc(minuend, subtrahend):  # 3
    difference = minuend - subtrahend
    print(difference, end="\n")


def do_divide(dividend, divisor):  # 4
    quotient = dividend / divisor
    return quotient


def nest_1(thewords):  # 5
    return thewords


def nested_def(ones, twos):  # 6
    print(nest_1(ones) * twos, end="\n")


def da_puntion(bossmam1, bossmam2, bossmam3):  # 7
    print(f"The fave food of bossmam is {bossmam1[2]} and  {bossmam2} is the favorite also " + bossmam1[0])
    print("brrrrr " + bossmam3)


lailai = ['rawberry', 'nanana', 'vavado']
da_puntion(lailai, "doomsdaybuddy", bossmam3='ate laiza')

do_da_math(2, 4, 6)
do_mor_math(3, 5)

print("Input minuend:", end='\n')
subtracc = int(input('>'))
do_subtracc(subtracc, 5)

divided = do_divide(4 + 12, 8)
print("The quotient is: {}" .format(divided))

twoooo = int(input('pick a number!'))
nested_def('beep bop ', twoooo)


for num in range(twoooo):  # 8
    nested_def('beep bop ', twoooo)


def dadada(*doodoo):  # 9
    print(doodoo[1])


def superclean(thing1, thing2, thing3):  # 10
    print(f"thess are the {thing1}, {thing2}, and {thing3}")


dadada("bean", "peanut", "chip")
superclean(thing1 = 'artemis', thing2 = 'police', thing3 = 'stay woke')

"""Arbitrary Keyword Arguments, **kwargs
If you do not know how many keyword arguments that will be passed into your function, 
add two asterisk: ** before the parameter name in the function definition."""


def my_function(**kid):
  print("His last name is " + kid["lname"])


my_function(fname = "Tobias", lname = "Refsnes")


def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result


print("\n\nRecursion Example Results")
tri_recursion(6)