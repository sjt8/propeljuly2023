# accept percentage from the user and display the grade

def compute_grade(mark):
    if mark > 90:
        return "A"
    elif mark > 80 and mark <= 90:
        return "B"
    elif mark > 60 and mark <= 80:
        return "C"
    else:
        return "D"


percentage = int(input("Enter your percentage: "))
grade = compute_grade(percentage)

print("Your Grade is: ", grade)