name=input("enter student name:")

sub1=int(input("subject 1 Marks:"))
sub2=int(input("subject 2 Marks:"))
sub3=int(input("subject 3 Marks:"))

total=sub1+sub2+sub3
average=total/3
percentage=(total/300)*100

print("student name:",name)
print("Total:",total)
print("Average:",average)
print("Percentage:",percentage)
if percentage>=35:
    print("pass")
else:
    print("fail")
