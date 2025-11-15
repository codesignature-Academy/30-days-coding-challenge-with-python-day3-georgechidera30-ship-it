CUTOFF_MARKS = {
    "medicine": 280,
    "law": 270,
    "engineering": 260,
    "computer science": 250,
    "business administration": 240,
    "economics": 230,
    "mass communication": 220,
    "sociology": 200
}
# Get student input
jamb_score = int(input("Enter your JAMB score: "))
department = input("Enter your preferred department: ").lower().strip()

# Check admission eligibility
if department in CUTOFF_MARKS:
    cutoff = CUTOFF_MARKS[department]
    
    if jamb_score >= cutoff:
        # Format department name for display (capitalize first letters)
        dept_display = department.title()
        print(f"Congratulations, you are admitted into {dept_display}!")
    else:
        dept_display = department.title()
        print(f"Sorry, you were not admitted into {dept_display}.")
        print(f"Required cut-off: {cutoff}, Your score: {jamb_score}")
        print(f"You need {cutoff - jamb_score} more points to meet the requirement.")

else:
    print("Invalid department entered!")
    print("\nAvailable departments:")
    for dept in CUTOFF_MARKS:
        print(f"- {dept.title()} (Cut-off: {CUTOFF_MARKS[dept]})")