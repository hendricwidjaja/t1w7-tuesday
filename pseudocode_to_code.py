numbers = [1, 2, 3, 4, 5]

total_sum = 0

for number in numbers:
    total_sum += number

print(total_sum)

max_number = numbers[0]

for number in numbers:
    if number > max_number:
        max_number = number

print(max_number)