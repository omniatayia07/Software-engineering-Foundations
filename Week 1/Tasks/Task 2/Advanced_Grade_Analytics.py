All = []

def Student(name, A, E, M, Ch):
    if A > 100 or A < 0 or E > 100 or E < 0 or M > 100 or M < 0 or Ch > 100 or Ch < 0:
        print("Error: Scores must be between 0 and 100. Student not saved.")
        return 

    total = A + E + M + Ch
    cnt = 4
    score = total / cnt

    print(name, ", Your average grade is:", score)

    if score >= 95:
        grade = "A+"
    elif score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B+"
    elif score >= 75:
        grade = "B"
    elif score >= 70:
        grade = "C+"
    elif score >= 65:
        grade = "C"
    elif score >= 60:
        grade = "D+"
    elif score >= 55:
        grade = "D"
    else:
        grade = "F"

    print("Your grade:", grade)

    Stu = {name: {"Arabic": A, "English": E, "Math": M, "Chemistry": Ch, "Average": score, "Grade": grade}}
    All.append(Stu)

while True:
    print("--- Enter Student Data ---")
    name = input("Enter your name: ")
    A = float(input("Enter your Arabic score: "))
    E = float(input("Enter your English score: "))
    M = float(input("Enter your Math score: "))
    Ch = float(input("Enter your Chemistry score: "))

    Student(name, A, E, M, Ch)
    print("Do you want to add another student?")
    print(" Yes:1 ")
    print(" No: 2  ")

    more = input("  ")
    if more != "1":
        break

print("--- Student Search Feature ---")
search_name = input("Enter student name to search for their data: ")

found = False  

for s in All:
    if search_name in s:
        print("Data found for", search_name, ":")
        print(s[search_name])
        found = True
        break  

if found == False:
    print("Sorry, this student does not exist in our records.")

print("Thank you! .")