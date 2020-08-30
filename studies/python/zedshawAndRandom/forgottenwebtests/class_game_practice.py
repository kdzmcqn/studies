def jello(name='Tam'):
    def greet():
        return 'Jello '+ name

    if name =='Tam':
        return greet
    else:
        return 'yo'


x = jello()
print(x())

def wasup():
    return 'gudnyt'

def other(func):
    return func()

print(other(wasup))


def a_decor(func):
    def resides_the_func():

        func()

    return resides_the_func

def this_the_func():
    print('yo')

def somefunc():
    print('not yo')


this_the_func = a_decor(this_the_func)

this_the_func()

def dec_orator(func):
     def do_func():
        print("decorator kasi pwede lagyan")
        func()
        print(f"ng mga print kung OPS! error {func.__name__} saan saan")
     return do_func

@dec_orator
def eyoo():
    print('yo-ness')

@dec_orator(somefunc)
def lala():
    print("print ka lang geh")


eyoo()
lala()