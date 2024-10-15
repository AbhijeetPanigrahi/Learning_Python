# Install a library from PyPi
# In the pypi website, search 'prettytable' and go to homepage which is at the left navbar.

from prettytable import PrettyTable

table = PrettyTable()
print(table)

table.field_names = ["City name", "Area", "Population", "Annual Rainfall"]
table.add_row(["Adelaide", 1295, 1158259, 600.5])
table.add_row(["Brisbane", 5905, 1857594, 1146.4])
table.add_row(["Darwin", 112, 120900, 1714.7])
table.add_row(["Hobart", 1357, 205556, 619.5])
table.add_row(["Sydney", 2058, 4336374, 1214.8])
table.add_row(["Melbourne", 1566, 3806092, 646.9])
table.add_row(["Perth", 5386, 1554769, 869.4])
print(table)


# Create another table for Pokemons

table1 = PrettyTable()
# row by row
table1.field_names = ["Pokemon Name", "Type"]

table1.add_row(["Pikachu", "Electric"])
table1.add_row(["Squirtle", "Water"])

print(table1)


table2 = PrettyTable()
# column by column
table2.add_column("Pokemon Name", ["Pikachu", "Electric"])
table2.add_column("Type", ["Squirtle", "Water"])

print(table2)

print(table2.align) # {'base_align_value': 'c', 'Pokemon Name': 'c', 'Type': 'c'}
# c -> center

table2.align = 'l'
print(table2)