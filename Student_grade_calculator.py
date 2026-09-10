print("===== Student Grade Calculator =====")

name = input("Enter student name: ")

english = int(input("Enter English marks: "))
maths = int(input("Enter Maths marks: "))
computer = int(input("Enter Computer marks: "))
science = int(input("Enter Science marks: "))
hindi = int(input("Enter Hindi marks: "))

total = english + maths + computer + science + hindi
percentage = (total / 500) * 100

if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"

print("\n===== Result =====")
print("Student Name:", name)
print("Total Marks:", total, "/ 500")
print("Percentage:", percentage, "%")
print("Grade:", grade)
