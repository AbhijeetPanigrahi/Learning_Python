# ATTRIBUTES

class Car1:
    pass

car_1 = Car1()

car_1.id = 221
car_1.model = 'lambo'

print(car_1.id)


# CONSTRUCTOR

class Car2:
    def __init__(self):
        print("A constructor is created")

car_2 = Car2()  # A constructor is created

car_3 = Car2()  # A constructor is created

class Car3:
    def __init__(self, car_id, model):
        self.id = car_id
        self.model = model
        self.wheels = 4

car_4 = Car3(414, 'audi')
# car_4 = Car3()    (It will show error messages since no parameters given)

print(car_4.id)     # 414
print(car_4.model)  # audi
print(car_4.wheels) # 4


# ADDING METHOD TO CLASS

class Car4:
    def enter_race_mode(self):
        self.seats = 2

car_5 = Car4()

car_5.enter_race_mode()
print(car_5.seats) # 2 


