print("--- Create Your Password ---")

while True:
    password = input("Enter a new password: ")
    
    # Check 1: Length
    if len(password) < 8:
        print("Error: Password must be at least 8 characters.")
        continue # Restart loop
        
    # Check 2: Spaces
    if " " in password:
        print("Error: Password cannot contain spaces.")
        continue # Restart loop

    # Check 3: Symbol
    if "@" not in password:
        print("Error: Password must contain the '@' symbol.")
        continue # Restart loop
        
    # If we get here, all checks passed
    print("Password saved successfully!")
    break # Exit the loop