from Armstrong import is_armstrong


lower = int(input("Enter the lower limit: "))
upper = int(input("Enter the upper limit: "))


print(f"Armstrong numbers between {lower} and {upper}:")
for num in range(lower, upper + 1):
    if is_armstrong(num):
        print(num)

	
