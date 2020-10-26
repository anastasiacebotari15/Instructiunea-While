"""Elaborați un program care va calcula suma, produsul și media aritmetică a numerelor de la 
1 la n, pentru n introdus de la tastatură."""
n=eval(input('Introduceti un numar:'))
i=0
s=0
p=1

while i<n:
    i+=1
    s+=i
    p*=i

print(f'Suma={round(s, 2)}',f'Produsul={round(p, 2)}',f'Media aritmetica={round(s/i, 2)}', sep='\n')