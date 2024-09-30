states_of_India = ["Odisha", "Gujurat" , "Goa"]
print(states_of_India)  # ["Odisha", "Gujurat" , "Goa"]
print(states_of_India[0])
print(states_of_India[-1])

states_of_India[1] = "Maharashtra"
print(states_of_India)  # ['Odisha', 'Maharashtra', 'Goa']

states_of_India.append("J&K")
print(states_of_India) # ['Odisha', 'Maharashtra', 'Goa', 'J&K']

states_of_India.extend(["AP" , "MP" , "Bihar"])
print(states_of_India) # ['Odisha', 'Maharashtra', 'Goa', 'J&K', 'AP', 'MP', 'Bihar']


# For more methods, go check out in the PYHON documentation