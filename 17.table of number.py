# Get input from user
n = int(input("Enter a number: "))

# Print multiplication table
print(f"Multiplication Table of {n}:")
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")
