"""Se citesc numere de la tastatură până la introducerea unui număr impar divizibil cu 3. 
Să se afişeze suma tuturor numerelor pare introduse."""
x=eval(input('Introduceti un numar:'))
s=0

while x%2==0 or (x%2!=0 and x%3!=0):
    if x%2==0:
        s+=x
    
    x=eval(input('Introduceti un numar:'))

print('Suma numerelor pare introduse:',s)