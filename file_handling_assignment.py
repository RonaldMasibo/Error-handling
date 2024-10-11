
# Open the file
my_file = open("my_file.txt", "a")

# Writing text to the file
my_file.write("I am in Africa.")
my_file.write("I am from Kenya.")
my_file.write("Kenya has 47 counties.")

# Closing the file
my_file.close()

# File reading & display
content = open("my_file.txt", "r")
read_file = content.read()
print(read_file)

# Error handling
try:
    value = 10/0
    number = int(input("Enter a number"))
    print(number)
except ZeroDivisionError:
    print("Value divided by Zero")