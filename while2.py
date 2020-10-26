"""Se citesc pe rând temperaturile medii ale fiecărei luni a unui an, ca numere întregi. 
Să se afişeze cu două zecimale media anuală a temperaturilor pozitive şi a celor negative.""" 
n=0
sumpoz=0
sumneg=0
nrpoz=0
nrneg=0
l=0

while l<12:
    n=eval(input('Introduceti temperatura:'))
    if n<55 and n>-60:
        l+=1
        if n>0:
            sumpoz+=n
            nrpoz+=1
        elif n<0:
            sumneg+=n
            nrneg+=1 
    else: print('Error: Introduceti o temperatura valida')           

if nrpoz>0:
    print('MediePoz=',round(float(sumpoz/nrpoz), 2))
else:print('Nu au fost temperaturi pozitive')

if nn>0:
    print("MedieNeg=",round(float(sumneg/nrneg), 2))
else:print("Nu au fost temperaturi negative")