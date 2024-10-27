# Get user input for the first number
num1 = int(input("Enter the first number: "))

# Get user input for the second number
num2 = int(input("Enter the second number: "))

# Calculate and print the sum
print("Sum:", num1 + num2)

# Calculate and print the difference
print("Difference:", num1 - num2)

# Calculate and print the product
print("Product:", num1 * num2)

#Calculate and print the quotient
#print("Quotient:", num1 / num2 ) # simple way for quotient formula but if num2 is zero it will be an error

# Calculate and print the quotient, handling division by zero
if num2 != 0: # if num2 is not equal to zero print undefined this because devided by zero is error,
    print("Quotient:", num1 / num2)
else:
  print("Quotient: Undefined (division by zero)")
