
my_values = []

def get_values():
    temp_value = ""
    while temp_value != "0":
        temp_value= input("Enter a number: ")
        my_values.append(temp_value)
    print(my_values)
        

def add_numbers():
    sum = 0
    for value in my_values:
        sum += int(value)
    return sum

def average_numbers():
    return add_numbers() / len(my_values)

def get_result():
    print("The sum is: " + str(add_numbers()))
    print("The average is: " + str(average_numbers()))
    
def main():
    get_values()
    get_result()

main()