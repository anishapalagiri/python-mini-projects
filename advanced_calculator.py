num1=float(input("enter the first number:"))
num2=float(input("enter the second number:"))
print("1.Addition")
print("2.Substraction")
print("3.Multiplication")
print("4.Division")
choice=int(input("enter choice:"))
if choice==1:
    print("Result=",num1+num2)
elif choice==2:
    print("Result=",num1-num2)
elif choice==3:
    print("Result=",num1*num2)
elif choice==4:
    print("Result=",num1/num2)
else:
    print("Invalid choice")