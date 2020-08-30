try:
    num = int(input('enter number: '))
    assert num % 2 == 0, 'you entered an odd number'
except AssertionError as obj:
    print(obj)

print('after the assertion')