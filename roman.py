#konvertuoja skaicius i romeniskus
def apskaiciavimas(skaicius,a,b,c,d):
    if skaicius == 9:
        print(a,end='')
    elif skaicius > 4:
        print(b, end='')
        while skaicius > 5:
            print(c, end='')
            skaicius = skaicius - 1
    if skaicius == 4:
        print(d, end='')
    elif skaicius < 4:
        while skaicius > 0:
            print(c,end='')
            skaicius = skaicius - 1


skaicius = input("Iveskite skaiciu:")
ilgis = len(skaicius)

if ilgis > 3:
    numberone = int(skaicius[0])
    numbertwo = int(skaicius[1])
    numberthree = int(skaicius[2])
    numberfour = int(skaicius[3])
    while numberone > 0:
        print('M',end='')
        numberone = numberone - 1
    apskaiciavimas(numbertwo,'CM','D','C','CD')
    apskaiciavimas(numberthree,'XC','L','X','XL')
    apskaiciavimas(numberfour,'IX','V','I','IV')
elif ilgis > 2:
    numberone = int(skaicius[0])
    numbertwo = int(skaicius[1])
    numberthree = int(skaicius[2])
    apskaiciavimas(numberone,'CM','D','C','CD')
    apskaiciavimas(numbertwo,'XC','L','X','XL')
    apskaiciavimas(numberthree,'IX','V','I','IV')
elif ilgis > 1:
    numberone = int(skaicius[0])
    numbertwo = int(skaicius[1])
    apskaiciavimas(numberone,'XC','L','X','XL')
    apskaiciavimas(numbertwo,'IX','V','I','IV')
elif ilgis > 0:
     numberone = int(skaicius[0])
     apskaiciavimas(numberone,'IX','V','I','IV')  
