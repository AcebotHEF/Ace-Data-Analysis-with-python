print("Welcome to the Tip Calculator!")

# 1. Get Inputs (and cast to float/int immediately)
bill = float(input("What was the total bill? $"))
tip_percent = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

# 2. Calculations
# Calculate tip amount
tip_amount = bill * (tip_percent / 100)

# Calculate total bill
total_bill = bill + tip_amount

# Calculate split
bill_per_person = total_bill / people

# 3. Output (Round to 2 decimal places)
# We use f-strings (formatted strings) for cleaner output
print(f"Each person should pay: ${round(bill_per_person, 2)}")