student_dict = {
    "student" : ["Sam", "Uman", "Hans", "David"],
    "score" : [56,45,89,75]
}

# Looping through dictionary
for (key, value) in student_dict.items():
    print(f"{key}: {value}")
# Output:
'''
student: ['Sam', 'Uman', 'Hans', 'David']
score: [56, 45, 89, 75]
'''

import pandas

student_dataframe = pandas.DataFrame(student_dict)
print(student_dataframe)

# Output:
'''
  student  score
0     Sam     56
1    Uman     45
2    Hans     89
3   David     75
'''

# loop through rows of a dataframe (using 'iterrows()')

for (index, row) in student_dataframe.iterrows():
    print(row) # each row is a pandas series

for (index, row) in student_dataframe.iterrows():
    print(f"Index: {index}, Student: {row['student']}, Score: {row['score']}")
