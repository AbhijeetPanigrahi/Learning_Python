def police_check(age:int) -> bool:  # it says the input must be a int and the output must be a boolean
    if(age>18):
        return True
    else:
        return False

print(police_check("Abhijeet")) # It will show error, since you already declared that the parameter must be int (age:int)