import pandas

data = pandas.read_csv("Samsung_Prism.csv")
print(data[data["Student Name"] == "ABHIGYAN MOHANTA"])
print(data[data["Student Name"] == "ABHIJEET PANIGRAHI"])
print(data[data["Student Name"] == "SARTHAK SAMBIT KAR"])
print(data[data["Student Name"] == "RITWIK ROUT"])
print(data[data["Student Name"] == "RASHMI RANJAN SAHOO"])
print(data[data["Student Name"] == "PRATIK KUMAR SAHOO"])
print(data[data["Student Name"] == "AKASH KUMAR LENKA"])
print(data[data["Student Name"] == "SOUMYA RANJAN PANDA"])

