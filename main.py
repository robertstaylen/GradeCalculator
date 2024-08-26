#user input (grades)
homework_grade = int(input("What is your homework grade?: "))
project_grade = int(input("What is your project grade?: "))
exam_grade = int(input("What is your exam grade?: "))
quiz_grade = int(input("What is your quiz grade? "))

#final grade calculation
final_grade = 0.40 * homework_grade + 0.30 * project_grade + 0.20 * exam_grade + 0.10 * quiz_grade
print("Your final grade is: "+ str(final_grade)) #final grade 