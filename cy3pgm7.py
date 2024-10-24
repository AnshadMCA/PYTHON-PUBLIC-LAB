
n = int(input("Enter a number to find its factors: "))


i = 1


print(f"Factors of {n} are:")
while i <= n:
    if n % i == 0:
        print(i)  
    i += 1 

