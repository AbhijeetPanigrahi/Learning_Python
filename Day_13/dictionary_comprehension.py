# new_dict = {new_key:new_value for item in list}
# new_dict = {new_key:new_value for (key,value) in dict.items()}

# Example: Convert a list into a dictionary (here we looped through the list)

students = ["John", "Mohn", "Jenny", "Menny"]
import random
students_scores = {student:random.randint(1,100) for student in students}
print(students_scores)

# Example: (here we will loop through the dictionary)

passed_students = {student:score for (student,score) in students_scores.items() if score>90}
print(passed_students)