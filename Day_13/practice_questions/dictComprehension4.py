# Character Position Mapping with Nested Dictionary
# Given a string, create a dictionary where the keys are the unique characters in the string, and the values are dictionaries containing the positions (indices) of those characters in the string.
# Example:-
# sentence = "comprehension"
# Output:-
'''
{
 'c': {'count': 1, 'positions': [0]},
 'o': {'count': 2, 'positions': [1, 11]},
 'm': {'count': 1, 'positions': [2]},
 'p': {'count': 1, 'positions': [3]},
 'r': {'count': 1, 'positions': [4]},
 'e': {'count': 2, 'positions': [5, 9]},
 'h': {'count': 1, 'positions': [6]},
 'n': {'count': 2, 'positions': [8, 12]},
 's': {'count': 1, 'positions': [10]}
}
'''
sentence = "comprehension"
char_positions = {char: {"count": sentence.count(char), 
                         "positions": [i for i, c in enumerate(sentence) if c == char]} 
                  for char in set(sentence)}
print(char_positions)
