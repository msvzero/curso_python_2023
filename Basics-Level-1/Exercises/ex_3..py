#Create a list of 4 numbers and then find the sum and average of the numbers
values_list = []
value_1 = input("Enter a number: ")
values_list.append(value_1)
value_2 = input("Enter another number: ")
values_list.append(value_2)
value_3 = input("Enter another number: ")
values_list.append(value_3)
value_4 = input("Enter another number: ")
values_list.append(value_4)

sum = int(value_1) + int(value_2) + int(value_3) + int(value_4)
average = sum / len(values_list)

print("The sum is: " + str(sum))
print("The average is: " + str(average))