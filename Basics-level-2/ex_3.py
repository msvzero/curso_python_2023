values_list = []
value_1 = input("Enter a number: ")
values_list.append(value_1)
value_2 = input("Enter another number: ")
values_list.append(value_2)
value_3 = input("Enter another number: ")
values_list.append(value_3)
value_4 = input("Enter another number: ")
values_list.append(value_4)

def add_numbers():
    sum = int(value_1) + int(value_2) + int(value_3) + int(value_4)
    return sum

def average_numbers():
    return add_numbers() / len(values_list)

def get_result():
    print("The sum is: " + str(add_numbers()))
    print("The average is: " + str(average_numbers()))

get_result()