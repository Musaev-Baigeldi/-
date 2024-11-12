numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

#missing_number = numbers.index(None)
#sum_of_numbers = sum(numbers[::missing_number]+numbers[missing_number+1:])
missing_index = numbers.index(None)

#print(sum_of_numbers)
sum_of_numbers = sum(numbers[:missing_index] + numbers[missing_index + 1:])
count_of_numbers = len(numbers)
average_value = round(sum_of_numbers / count_of_numbers, 2)
numbers[missing_index] = average_value
print("Измененный список:", numbers)
