#1 ----------

def names(a=1, b=2, c=0):
    print(a , b , c)
names(5)

def names1(a, b=2, c=9):
    print(a , b , c)
names1(5)

#2 --------

def add(*args):     # unlimited arguments
    sum = 0
    for n in args:
        # print(n)
        sum += n
    return sum
print(add(1, 2, 3, 4, 5))  


#3 -----------

def calculate(**kwargs):        # key word arguments
    print(kwargs)
    for key,value in kwargs.items():
        print(key)
        print(value)
calculate(a=1, b=2, c=3, d=4)   #  print a dictionary

def calculate(n,**kwargs):        
    print(kwargs)
    n += kwargs["a"]
    n *= kwargs["b"]
    print(n)
calculate(2, a=1, b=2, c=3, d=4)   


#4 -----------

# What is the output of this code?
def bar(spam, eggs, toast='yes please!', ham=0):
    print(spam, eggs, toast, ham)
 
bar(toast='nah', spam=4, eggs=2) 

def test(*args):
    print(args)
 
test(1,2,3,5)
# What is the data type of args? (Ans - tuple)

def all_aboard(a, *args, **kw): 
    print(a, args, kw)
 
all_aboard(4, 7, 3, 0, x=10, y=64)

# What is the output of the code above?  ( Ans - 4 (7,3,0) {'x':10 ,'y':64} )

