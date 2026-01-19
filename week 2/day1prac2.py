# A simple grading System

score = 65

if score >= 90: # 1st condition
    print("Grade: A")
elif score >= 80: # 2nd condition
    print("Grade: B")  # This runs because 85 >= 80
elif score >= 70: # 3rd condition
    print("Grade: C")
elif 60 <= score < 70: # 4th condition
    print("Grade: C2")
else:
    print("Grade: F")