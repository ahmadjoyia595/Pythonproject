f=open("students_grades.txt", "w")
f.write("Alice, 85 \n")
f.write("Bob, 92 \n")
f.write("Charlie, 76 \n")
f.write("Daisy, 55 \n")
f.write("Eve, 90 \n")
f.close()

f=open("students_grades.txt", "r")
students=f.readlines()
g=open("students_results.txt" , "w")


for student in students:
    name , grade =student.strip().split(',')
    grade=int(grade)
    if grade >= 60 :
        print(f"{name} has passed with a grade of {grade}.\n")
    else:
        print(f"{name} has failed with a grade of {grade}.\n")
g.close()

g=open("students_results.txt" , "r")
print(g.readlines())