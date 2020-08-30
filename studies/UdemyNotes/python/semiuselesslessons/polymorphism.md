# Polymorphism
1. Duck Typing
2. Dependency Injection
3. Method Overriding

## Duck Typing
```
def callTalk(obj):
    obj.talk()
```
```mermaid
graph BT
calltalk-->hello & quack
    subgraph Duck
        quack
    end
    subgraph Human
        hello
    end
```
## Demo
```
class Duck:
    def talk(self):
        print("Quack")


class Human:
    def talk(self):
        print("Hello")


def callTalk(obj):
    obj.talk()


d = Duck()
callTalk(d)

h = Human()
callTSalk(h)
```
## Dependency Injection
```mermaid
graph BT
    AirbusEngine-->Engine
    BoingEngine-->Engine
    Engine-->Flight
```
Injecting ang object into another object.