print("Welcome to the tip calculator")
total = float(input("what was the total bill? $"))
tip = int(input("What percentage of tip would you like to give? (10 12 15) "))
people = int(input("How many people to split the bill? "))
tip_as_percentage = tip/100
total_tip_amt = total*tip_as_percentage
total_bill = total + total_tip_amt
bill_per_person = total_bill / people
final_amt = round(bill_per_person, 2)
print(f"Each person should pay: ${final_amt}")