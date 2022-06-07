import time

print("Welcome to the Tip Calculator")
bill = float(input("What was the total bill ?\n $"))
tip = int(input("How many tip would you like to give ? .. 10,15 or 20 "))
people = int(input("How many people to split the bill ?"))
time.sleep(0.5)

tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)

print(f"The total bill include {tip} % of tip is {total_bill} $")
time.sleep(0.5)
print(f"Each person should pay : ${final_amount}")