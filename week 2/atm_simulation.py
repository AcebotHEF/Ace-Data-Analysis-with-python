# ATM Cash Dispensing Simulation (WHILE LOOP)
# Rules
# Amount must be divisible by 1000
# ATM uses highest denomination first
# If amount is invalid → reject
# Output number of notes for each denomination

amount = 37000
denominations = [10000, 5000, 1000]

if amount <= 0 or amount % 1000 != 0:
    print("Invalid amount")

else:
    remaining = amount

    for note in denominations:
        count = 0

        while remaining >= note:
            remaining -= note
            count += 1

        if count > 0:
            print(f"{note}: {count}")
