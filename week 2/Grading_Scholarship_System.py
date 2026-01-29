# Intelligent Student Grading & Scholarship System 

scores = [78, 82, 69, 90, 74]
attendance_percentage = 88
disciplinary_cases = 0

status = "Pass"
scholarship = "Not Eligible"

# Attendance check
if attendance_percentage < 60:
    status = "Fail"
    grade = "N/A"

else:
    # Check for failing any subject
    for score in scores:
        if score < 40:
            status = "Fail"
            break

    average = sum(scores) / len(scores)

    if average >= 70:
        grade = "A"
    elif average >= 60:
        grade = "B"
    elif average >= 50:
        grade = "C"
    else:
        grade = "D"

    if (
        grade == "A"
        and attendance_percentage >= 85
        and disciplinary_cases == 0
        and status == "Pass"
    ):
        scholarship = "Eligible"

print("Grade:", grade)
print("Status:", status)
print("Scholarship:", scholarship)
