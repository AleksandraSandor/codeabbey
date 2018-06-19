import copy
dane = []
liczba_wierszy = int(input())
for x in range(liczba_wierszy):
    wiersz = input()
    lista_liczb_jako_str = wiersz.split(' ')
    lista_liczb_jako_int = list(map(int, lista_liczb_jako_str))
    dane.append(lista_liczb_jako_int)

print (dane)
dane_zrodlowe=tuple(dane)
dane_zrodlowe=copy.deepcopy(dane)
print ('ola')

lista = ['foobar']
enumerate(lista) == [(0, 'foobar')]
poz, x = (0, 'foobar')

#obliczanie GCD
#poz=0
def gcd(a,b):
    while a!=b:
        while a<b:
            b=b-a
            while a>b:
                a=a-b
        while a>b:
            a=a-b
            while a<b:
                b=b-a
    return a

def lcm(a,b,c):
    return (a*b)//c
    
# 1 sposób (gromadzimy dane w postaci 1 listy)              
#for poz,x in enumerate(dane):
#   GCD=gcd(x[0],x[1])
 #   dane_zrodlowe[poz].append(GCD)
  #  LCM=lcm(x[0], x[1], x[2])
   # dane_zrodlowe[poz].append(LCM)
    
#2 sposób (wyniki w nowej liście)  
wyniki=[]
for x in dane:
    GCD=gcd(x[0],x[1])
    LCM=lcm(x[0], x[1], GCD)
    wyniki.append((GCD,LCM))

print(wyniki)

lista=[]
for y in wyniki:
    k='(%s %s)' %(y[0], y[1])
    lista.append(k)

print(' '.join(lista))




