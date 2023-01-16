
def add_two_numbers():
    value_1 = input("Enter a number: ")
    value_2 = input("Enter another number: ")
    result = int(value_1) + int(value_2)
    return result

print("The result is: " + str(add_two_numbers()))