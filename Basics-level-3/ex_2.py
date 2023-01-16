
my_values = []

def get_values():
    for i in range(5):
        temp_value= input("Enter a number: ")
        my_values.append(temp_value)

def add_numbers():
    sum = 0
    for value in my_values:
        print("val: " + value)
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