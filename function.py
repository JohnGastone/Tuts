# A function is a block of code that perfoms a particular task
# Features / Characteristics of functions
# 1. Function declaration i.e. we use def() keyword to declare a function in Python
# 2. Function parameters i.e def kazi(mshahara, malupulupu)
# 3. Function call i.e. kazi(5000000, 1000000)
# 4. Return value i.e return mshahara
# 5. Reusability i.e Using the same function multiple times
# 6. Modularity i.e working on simplified smaller code blocks(functions) / modules
# 7. Abstractions i.e hiding the logic behind the code(complex implementations)

# FUNCTION  DECLARATION

def kazi():
    x = 3
    while x < 5:
        print("This is the function of while loop")
        x += 1
        if x == 4:
            print("++++++++++++++++++")
        elif x == 5:
            print("If the function execute this then we are out of while loop")


# FUNCTION CALL
kazi()


# Second Example

def kazi(mshahara, malupulupu):
    print(str(mshahara) + '  utakua mshahara wa hii kazi ' +
          'na malupulupu yake yatakua  ' + str(malupulupu))


kazi(5000000, 1000000)


# Arbitrary arguments, *args & Keyword arguments

def watoto(fName, mName, lName):
    print(fName,  mName, lName)


watoto(fName="Jafari", mName="Mwanayumba", lName="Hamisi")


# Arbitrary keyword arguments

def my_function(**kid):
    print("His first name is " + kid["fname"])


my_function(fname="Tobias", lname="Mwasege")
