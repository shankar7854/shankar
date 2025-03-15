class InvalidAgeError(Exception):
    def __init__(self, message="Age cannot be negative or too high"):
        self.message = message
        super().__init__(self.message)
def check_age(age):
    if age < 0:
        raise InvalidAgeError("Age cannot be negative.")
    elif age > 120:
        raise InvalidAgeError("Age cannot be greater than 120.")
    else:
        return f"Age {age} is valid."
try:
    age = int(input("Enter your age: "))
    result = check_age(age)
    print(result)
except InvalidAgeError as e:
    print(f"Error: {e}")
