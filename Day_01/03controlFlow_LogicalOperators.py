#   if/elif/else
height = int(input("What's your height?".lower()))
if height > 120: 
    age = int(input("what's your age?"))
    if age>20:
        print("You can ride the big rollercoaster")
        if age>65:
            print("Please pay 75$")
        elif age>50:
            print("Please pay 50$")
        elif age>=30 and age<=35:
            print("Enjoy the free ride")
        else:
            print("Please pay 25$")
    else:
        print("You can ride the small rollercoaster")
else:
    print("Sorry you have to grow taller before you can ride the rollercoaster")

#   if/elif/else