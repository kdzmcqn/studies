from functools import wraps

def loga(func):
    @wraps(func)
    def with_loggint(*args, **kwargs):
        print(func.__name__ + " was called.")
        return func(*args, **kwargs)
    return with_loggint

@loga
def addition_func(x):
    return x + x

result = addition_func(4)

print(result)


def logit(logfile='out.log'):
    def logging_decorator(func):
        @wraps(func)
        def wrapped_function(*args, **kwargs):
            log_string = func.__name__ + " was called."
            print(log_string)
            with open(logfile, 'a') as opened_file:
                opened_file.write(log_string + '\n')
        return wrapped_function
    return logging_decorator


@logit()
def myfunc1(x):
    return x

myfunc1(55)


@logit(logfile='func2.log')
def myfunc2(*yo):
    y = sum(yo)
    return y

myfunc2(1, 2, 3, 4)