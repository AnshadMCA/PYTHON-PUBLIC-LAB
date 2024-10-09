num1=input("Enter the first number:")
num2=input("Enter the Second number:")
num3=input("Enter the Third number:")
num1 = int(num1)
num2 = int(num2)
num3 = int(num3)

if num1>=num2 and num1>=num3:
    print(num1, "is the largest")
elif num2>=num1 and num2>=num3:
    print(num2, "is the largest")
else:
    print(num3, "is largest")


