def shankar(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True  # This should be outside the loop

number = int(input("Enter a number: "))
if shankar(number):
    print("The number is prime.")
else:
    print("The number is not prime.")
