def calculate_simple_interest(principal, time, is_senior):
    rate = 12 if is_senior else 10
    SI = (principal * rate * time) / 100
    return SI


principal = float(input("Enter the principal amount: "))
time = float(input("Enter the time in years: "))
is_senior = input("Is the customer a senior citizen? (yes/no): ").strip().lower() == "yes"


interest = calculate_simple_interest(principal, time, is_senior)
print("The simple interest is:", interest)

