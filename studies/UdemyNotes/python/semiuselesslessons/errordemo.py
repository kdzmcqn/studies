try:
    f = open('myfile', 'w')
    a, b = [int(x) for x in input("Enter two numbers: ").split()]
    c = a/b
    f.write("writing %d into file" %c)
    f.close()
except ZeroDivisionError:
    print("division by zero is not allowed")
else:
    print('you have entered a non-zero number')
finally:
    f.close()
    print('file closed')
print('code after the exception')
