"""Se introduc succesiv numere nenule până la introducerea numărului 0. Să se afişeze suma 
tuturor numerelor introduse."""
nr=eval(input('Introduceti un numar:'))
suma=0
while nr!=0:
    suma+=nr
    nr=eval(input('Introduceti un numar:'))

print('Suma nr introduse este:',suma)
