max = 5

total =0.0

print('This program calculates the sum of')
print(max,'numbers you will enter.')

for conter in range(max):
    number = float(input('Enter a number: '))
    total = total + number

print('The total is', total)