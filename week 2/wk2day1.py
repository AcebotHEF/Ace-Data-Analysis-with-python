age = int(input("Enter your age: "))
name = input("Enter your name: ")

if age >= 18:
    print(f"Hello, {name}! You are an adult.")
    print("You are eligible to vote.")
    print(f"You are {age} years old.")
    print("You are {age} years old.")
else:
    print(f"Hello, {name}! You are a minor.")
    print("You are not eligible to vote.")
    print(f"You are {age} years old.")