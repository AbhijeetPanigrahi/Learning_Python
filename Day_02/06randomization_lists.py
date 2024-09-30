#   Who will pay the Bill?
import random

friends = [ "John", "Mary", "kairo" , "George", "Vina" , "Tom"]

# option-1
print(f"{friends[random.randint(0, len(friends)-1)]} will pay the bill")

# option-2
print(f"{random.choice(friends)} will pay the bill")

