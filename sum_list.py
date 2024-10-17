numbers=[int (x) for x in input("Enter numbers (seperated by spaces):").split()]
total_sum=0
for num in numbers:
    total_sum += num
print(f"The sum of all items in the list is: {total_sum}")

