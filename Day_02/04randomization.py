import random
import my_module    # imported another file # type: ignore 
# random module
randomInteger = random.randint(1,10)

print(randomInteger)
print(my_module.my_favourite_number)

randomNumber_from_0_to_1 = random.random()  # use this always
print(randomNumber_from_0_to_1)

random_float = random.uniform(1,10)
print(random_float)

