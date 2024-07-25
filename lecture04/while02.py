keep_going = 'y'

while keep_going == 'y':
    sale = float(input('Enter the amount of the sale: '))
    comm_rate = float(input('Enter the commission rate: '))
    
    comission = sale * comm_rate

    print('The commission is $', format(comission, '.2f'))
    
    keep_going = input('Do you want to calculate another commission? (Enter y for yes): ')