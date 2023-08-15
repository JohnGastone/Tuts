# This file is all about Dictionaries

# These are built-in data type used to store items in key : value pair.
# Features/Characteristics of Dictionary
# 1. Dict items are Ordered
# 2. Dicts are changeable
# 3. Dicts do not allow duplicates

#  Declaring a dictionary
Kiswahili = {
    'Nomino': 'Chakula',
    'Kivumishi': 'Safi',
    'Kitenzi': 'Pika',
    'Lafudhi': 120,
    'Mofimu': 'Tegemezi',
    'Ngeli': 'YU-A-WA',
    'Maokoto': 'Pesa'
}
print(Kiswahili)
# Dictionary can also be created using a dict() constructor

myDict = dict(name='John', age=40, IQ=0, nationality='Zimbabwean')

print(myDict)
# Accessing dictionary items

funguo = Kiswahili.keys()
print(funguo)
items = Kiswahili.values()
print(items)
dicti = Kiswahili.items()
print(dicti)
# Checking the presence of a value in the dictionary
if 'name' in myDict:
    print('John exists in the dictionary world')
else:
    print('John is illusional')
# Changing Dict Values
Kiswahili['Ngeli'] = 'KI-ZI'
Kiswahili['Kitendawili'] = 'Tega'
Kiswahili.update({'Sanaa': 'Muziki'})
Kiswahili.popitem()
print(Kiswahili)

# del (Kiswahili)
# print(Kiswahili)


for x in Kiswahili:
    print('Hii ipo')
