# Lambdas
+ Anonymous functions **have no name**
## Use
### Normal function
```
def square(x):
    return x*x
```
### Lambda Function
```
lambda x: x*x
```

## Declaration
+ starts wiht word 'lambda'
    ```
    lambda *args: expression
    ```
### rare use
```
f = lambda x: x*x
results = f(10)
```
### useful
+ filter
+ map
+ reduce

## create lambda to calculate cube
```
def cube(n):
    return n**3


# lambda
f = lambda n: n**3
print(f(2))
```

## lambda yes(even) or no(odd)
```
lambda x: 'yes' if x%2==0 else 'no'
```
## lambda sum of 2 numbers
```
lambda x,y: x+y
```

## using filter function
```
lst = [2,5,6,7]
result = list(filter(lambda x: x % 2 == 0, lst))
print(result
```
## using map function
```
lst = [2,3,4,5]
result = list(map(lambda n: n*2, lst))
print(result)
```
## reduce calc sum of given list
```
from functools import reduce
lst = [5,10,15,20]
result = reduce((lambda x,y: x+y), lst)
print(result)
```