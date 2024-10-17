class Animal:
    def __init__(self):
        self.num_eyes = 2
    def breathe(self):
        print("Inhale, Exhale.")

# class Fish:
#     def swim(self):
#         print("moving in water.")

# To make this Fish class an inheritanc eof Animal class:

class Fish(Animal):

    def __init__(self):
        super().__init__()
    def swim(self):
        print("moving in water.")

    # creating the same method 'breathe' but doing some extra work:

    def breathe(self):
        super().breathe()
        print("Doing under water.")

nemo = Fish()
nemo.swim()

nemo.breathe()