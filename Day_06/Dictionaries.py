persons = { 'name' : "Ram" , 'age' : 22 , 'height' : 5.8 }

print(persons['name'])

persons['weight'] = 68

print(persons)

for key in persons :
    print(f"{key} : {persons[key]}")