# What is python?
+ Interpreted **no additional step compilation**
+ Functional 
+ Object-Oriented Language
+ Simple-syntax
+ Fast-Inbuilt Libraries
# Why python?
+ Very easy to learn
+ Good performance
+ Dynamically Typed **no need to specify the data type**
# Tuple
+ cannot be modified **immutable**
  + cannot use `append() clear()`
  ## List to tuple
    ```
    tuple(list_name) # 1
    tuple(i for i in list_name) #2
    (*list_name, )    
    ```
# Set
+ If we add elements multiple times, it will not duplicate
+ No indexing *does not support indexing*
+ No slicing *not subscriptable*
+ No repition *unsupported operand types*
## to add/remove elements/
```
s.update([88,99])
s.remove()
```
## Convert Set to Frozenset
```
f = frozenset(s)
```
+ does not support update *no attribute called Remove/Update*

# Command Line Arguments
```
python app.py arg1 agr2 arg3...
```