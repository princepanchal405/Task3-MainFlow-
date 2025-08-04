numbers = [10, 20, 4, 45, 99]

# Remove duplicates and sort in descending order
unique_numbers = list(set(numbers))
unique_numbers.sort(reverse=True)

# Get second largest
if len(unique_numbers) >= 2:
    print("Second largest number is:", unique_numbers[1])
else:
    print("List doesn't have enough unique elements.")
