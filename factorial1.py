number=int(input("enter a number:"))
factorial=1
for i in range(2,number+1):
    factorial *=i
print(f"The factorial of {number} is {factorial}")
