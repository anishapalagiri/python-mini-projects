def calculate_total(marks):
    return sum(marks)
def calculate_average(total, subjects):
    return total / subjects
def calculate_grade(avg):
    if avg>=90:
        return "A+"
    elif avg>=80:
        return "A"
    elif avg>=70:
        return "B"
    elif avg>=60:
        return "C"
    elif avg>=50:
        return "D"
    else:
        return "Fail"
name=input("Enter student name:")
marks = []
for i in range(1,6):
    mark=int(input(f"Enter subject {i} marks: "))
    marks.append(mark)
total=calculate_total(marks)
average=calculate_average(total, len(marks))
grade=calculate_grade(average)
print("\n----STUDENT REPORT----")
print("Student Name:",name)
print("Marks:",marks)
print("Total",total)
print("Average:",average)
print("Grade:",grade)














