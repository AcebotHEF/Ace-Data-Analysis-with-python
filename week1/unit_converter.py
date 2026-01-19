print("--- Universal Unit Converter ---")

# Part 1: Distance
km = float(input("Enter distance in Kilometers: "))
miles = km * 0.621371
print(f"{km} KM is equal to {round(miles, 2)} Miles.")

print("-" * 20) # Prints a separator line

# Part 2: Temperature
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C is equal to {round(fahrenheit, 1)}°F.")