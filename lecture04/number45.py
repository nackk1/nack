colum = int(input("please nput the number of colum: "))
for number in range(1,101):
    print(number, end='\t')
    if number % colum == 0:
        print("")