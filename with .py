
user_text = input("Enter text to write to the file: ")


with open("output.txt", "w") as file:
    # Write the user input to the file
    file.write(user_text)

print("Text has been written to output.txt")
