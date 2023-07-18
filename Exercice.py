a,b = 6,10
def somme(a,b):
    return (a+b)

def subtract(a,b):
    return (a-b)


def division(a,b):
    return (a/b)

def multiplication(a,b):
    return (a*b)

print("select, operation")
print("1.add")
print("2.subtract")
print("3.multiplication")
print("4.division")
calcul= input("entre calcul(1/2/3/4):")
numbre1 = int(input("entre first number"))
number2 = int(input("entre second number:"))

if calcul == '1':
    print(numbre1,"+",number2,"=",somme(numbre1,number2))
elif calcul== '2':
    print(numbre1,"-",number2,"=",subtract(numbre1,number2))
elif calcul== '3':
    print(numbre1,"-",number2,"=",multiplication(numbre1,number2))

elif calcul== '4':
    print(numbre1,"-",number2,"=",division(numbre1,number2))
