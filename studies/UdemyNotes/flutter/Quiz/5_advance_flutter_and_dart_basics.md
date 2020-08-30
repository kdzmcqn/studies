# Advance Flutter & Dart Basics

## 1. What's special about this class?
~~~
class _Person{
    final _name = 'Max';
}
~~~

### Answer
It's a private class (with a private property) which can only be used in its own library/file

### Details
The leading "_" marks a class, property, or method as private, which means that you can only use it in the same library. Typicall, a file is treated as a separate library.


## 2. What's the idea behind an "enum"?

### Answer
An enum is a value where you can choose from multiple possible choices. You can choose by selecting a human-readable label, behind the scenes, the labels are mapped to integers (0, 1, ...).

### Details

## 3. What can `EdgeInsets.all(...)` be used for?

### Answer
Create an object with a special configuration/special default property values.

### Details
You can have more than one constructor in your Dart classes. Extra constructors typically yield you differently configured objects of the same type.

## 4. What's the difference between a `List` (`[]`) and a `Map` (`{}`) in Dart/Flutter?

### Answer
Lists gives you an ordered list of single values, identified by an index. Maps use key-value pairs where you identify values by their key

## 5. What does the following code snippet produce?
```
final names = ['Max', 'Manu', 'Julie'];
final results = names.map((name) => Text(name)).toList();
```

### Answer
`result` is a list of `Text()` widgets where each widget holds a different `name` from `names`

### Details
`map()` returns a new iterable (which is transformed to a list via `toList()`) where each value of the original list (`names`) is transformed as "*described*" by the function you pass to map. In this case, each `name` is wrapped into a `Text()` widget and then added to the new list which is stored in `result`.

## 6. What's true about `final`?

### Answer
Properties or variables marked as `final` can't change at runtime.

### Details
At runtime, an initial, dynamic value can be assigned, thereafter, the property/variable can't be changed again.