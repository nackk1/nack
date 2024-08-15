phonebook = {'Anirach': '777-111', 'Mickey': '777-2222', 'DOonald': '777-3333'}

print(phonebook)

print(phonebook('MIckey'))
print(phonebook.get('Donald'))

key = 'Phuto'
if key in phonebook:
    print(phonebook('Pluto'))
else:
    print(key + 'not in phonebook')

phonebook['Simpon'] = '777-4567'
phonebook['Pluto'] = '777-4444'
phonebook['Mickey'] = '777-2122'
print(phonebook)

del phonebook['Simpon']
print(phonebook)