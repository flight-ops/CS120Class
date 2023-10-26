numbers = [0]*5
another_numbers = [1,2,3]*5
print(numbers, another_numbers)

index = 0
while index < len(numbers):
    another_numbers[index] +=10
    index +=1

print (numbers + another_numbers)

piece_of_another_numbers = another_numbers[1:3]
print (piece_of_another_numbers)