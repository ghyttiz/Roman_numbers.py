#konvertuoja skaicius i romeniskus
def calculate(number,a,b,c,d):
    if number == 9:
        print(a,end='')
    elif number > 4:
        print(b, end='')
        while number > 5:
            print(c, end='')
            number = number - 1
    if number == 4:
        print(d, end='')
    elif number < 4:
        while number > 0:
            print(c,end='')
            number = number - 1


number = input("Please write number you want to be written in Roman numerals:")
length = len(number)

if length > 3:
    numberone = int(number[0])
    numbertwo = int(number[1])
    numberthree = int(number[2])
    numberfour = int(number[3])
    while numberone > 0:
        print('M',end='')
        numberone = numberone - 1
    calculate(numbertwo,'CM','D','C','CD')
    calculate(numberthree,'XC','L','X','XL')
    calculate(numberfour,'IX','V','I','IV')
elif length > 2:
    numberone = int(number[0])
    numbertwo = int(number[1])
    numberthree = int(number[2])
    calculate(numberone,'CM','D','C','CD')
    calculate(numbertwo,'XC','L','X','XL')
    calculate(numberthree,'IX','V','I','IV')
elif length > 1:
    numberone = int(number[0])
    numbertwo = int(number[1])
    calculate(numberone,'XC','L','X','XL')
    calculate(numbertwo,'IX','V','I','IV')
elif length > 0:
     numberone = int(number[0])
     calculate(numberone,'IX','V','I','IV')  
