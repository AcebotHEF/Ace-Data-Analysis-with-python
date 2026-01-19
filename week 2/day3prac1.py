# Example: Find the first even number greater than 3
for number in range(1, 10):
    if number <= 3:
        continue # Skip 1, 2, 3
    
    if number % 2 == 0:
        print(f"Found it: {number}")
        break # Stop searching after finding 4