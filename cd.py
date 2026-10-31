numbers = [10, 20, 30, 40, 50]

# Calculate the sum and divide by the count of items
if numbers:
    average = sum(numbers) / len(numbers)
    print(f"The average is: {average}")
else:
    print("The list is empty, cannot calculate average.")
