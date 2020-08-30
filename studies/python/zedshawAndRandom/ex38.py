ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there are not 10 things in that list. Let's fix it.")

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee",
              "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("Adding: ", next_one)
    stuff.append(next_one)
    print(f"There are {len(stuff)} items now.")

print("Let's do some things with stuff.")
print(stuff)
print(stuff[1])
print(stuff[-1])
print(stuff.pop())
print(' '.join(stuff))
print('#'.join(stuff[3:4]))  # [number:number] medj pareho sa range(start,end)
print('#'.join(stuff[3:5]))  # [3:5] hanggang 3 to 4 lang talaga
print('#'.join(stuff[3:6]))
print('#'.join(stuff[3:7]))
print('#'.join(stuff[3:8]))
print('#'.join(stuff[3:9]))
print(stuff)
