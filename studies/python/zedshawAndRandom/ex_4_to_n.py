cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print("There are", cars, "cars available.")
print("Tjere are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")

my_name = 'Leandro Lapena'
my_age = 25
my_height = 173 # cm
my_weight = 125 # lbs
my_eyes = 'Brown'
my_teeth = 'White'
my_hair = 'Black'

print(f"Let's talk about {my_name}.")
print(f"He's {my_height} centimeters tall.")
print(f"He's {my_weight} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {my_eyes} eyes and {my_hair} hair.")
print(f"His teeth are usually {my_teeth} depending on the cofee.")
total = my_age + my_height + my_weight
print(f'If I add {my_age}, {my_height}, and {my_weight} I get', total)
print("round of 1.7333", round(1.7333)) # 2
print("round of 1.333", round(1.333)) # 1
print("round of 1.5", round(1.5)) # 2
print("round of 1.49", round(1.49)) # 1

