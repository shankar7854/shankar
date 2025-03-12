# Define a list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use filter() to get even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

# Use map() to square each number in the list
squared_numbers = list(map(lambda x: x ** 2, numbers))

print("Original numbers:", numbers)
print("Even numbers:", even_numbers)
print("Squared numbers:", squared_numbers)
