
number = int(input('Enter a number: '))
fact = 1
for num in range(1, number + 1):
    fact *= num
print(f'Factorial: {fact}')
