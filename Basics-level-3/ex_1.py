#Compute the max value inside a list of numbers

test_values = [3, 5, 99, 9, 11, 13, 15, 17, 19, 21]

def max_value(values_list):
    max = values_list[0]
    for value in values_list:
        if value > max:
            max = value
    return max

print("The max value is: " + str(max_value(test_values)))