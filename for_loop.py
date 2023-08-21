# For loop statements
# For loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

x = ('Anna', 'Maokoto', 'Mwaisa')
for item in x:
    print(item)


mapochopocho = ['Biryani', 'Pilau', 'Wali nazi', 'Makange', 'Kitimoto']
# mapochopocho = masotojo.list()
for pochopocho in mapochopocho:
    print(pochopocho)
    print("It is true this " + pochopocho + ' is amazing')


switch_dict = {
    "case1": "This is case 1",  # This is the first case of the Switch statement
    "case2": "This is case 2",  # ----||-----
    "case3": "This is case 3"  # ----||-----
}

for case in switch_dict:
    print(case)
    if case == 'case1':
        pass
    if case in switch_dict:
        print('This is useless print statement')


for i in range(1, 10):
    print(i)
