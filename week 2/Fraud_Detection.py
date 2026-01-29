# Fraud Detection Using Transaction Streaks (FOR LOOP)
# 🧠 Scenario
# A bank wants to detect suspicious spending behavior.
# You are given a list of daily transactions.
# If 3 or more consecutive transactions are above ₦100,000, flag the account.

transactions = [45000, 120000, 130000, 150000, 40000, 200000]

streak = 0
start_index = -1
fraud_detected = False

for i in range(len(transactions)):
    if transactions[i] > 100000:
        if streak == 0:
            start_index = i
        streak += 1

        if streak == 3:
            fraud_detected = True
            break
    else:
        streak = 0

if fraud_detected:
    print("Fraud Detected")
    print("Started at index:", start_index)
else:
    print("No Fraud")
