account_balance = 300000
transaction_amount = 150000
transaction_type = "withdraw"
daily_withdrawn = 400000
is_verified = True

status = ""
final_balance = account_balance

if transaction_amount <= 0:
    status = "Transaction Failed: Invalid amount"

elif transaction_type == "withdraw":
    limit = 500000 if is_verified else 100000

    if not is_verified:
        status = "Transaction Failed: Account not verified"

    elif transaction_amount > account_balance:
        status = "Transaction Failed: Insufficient balance"

    elif daily_withdrawn + transaction_amount > limit:
        status = "Transaction Failed: Daily limit exceeded"

    else:
        final_balance -= transaction_amount
        status = "Transaction Successful"

elif transaction_type == "deposit":
    final_balance += transaction_amount
    status = "Transaction Successful"

else:
    status = "Transaction Failed: Invalid transaction type"

print(status)
print("Final Balance:", final_balance)
