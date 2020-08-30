# n size
n = 5

# SPACES
for i in range(n):
    print(' ' * i, end='')

    #Inverted odd pyramid
    for j in range(n-i,0,-1):
        print(f'{n-i}', end='')

    #NEXT LINE
    print('')

#Next code
print('')

#RIGHT TRIANGLE

#SPACES
for i in range(0,n):
    print(' '*(n-i-1), end='')

    #FORWARD COUNT
    for j in range(1,i+2):
        print(j, end='')

    #NEXT LINE
    print('')

#NEXT CODE
print('')

#SYMMETRIC PYRAMID

#SPACES
for i in range(0,n):
    print(' '*(n-i-1), end='')

    #FORWARD COUNT
    for j in range(1,i+2):
        print(j,end='')

    #BACKWRD COUNT
    # for j in reversed(range(1,i+2)):
    for j in range(i, 0, -1):
        print(j,end='')

    #NEXT LINE
    print('')


