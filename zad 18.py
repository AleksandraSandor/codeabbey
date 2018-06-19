dane = []
liczba_wierszy = int(input())
for x in range(liczba_wierszy):
    wiersz = input()
    lista_liczb_jako_str = wiersz.split(' ')
    lista_liczb_jako_int = list(map(int, lista_liczb_jako_str))
    dane.append(lista_liczb_jako_int)

print (dane)

def heron(x,n):
    if n==0:
        r=1
        return r
    else:
        r=1
        while n>0:
            d=x/r
            r=(r+d)/2
            n-=1
        return r

koncowe=[]
for x in dane:
    wyniki=heron(x[0], x[1])
    koncowe.append(wyniki)

print(koncowe)
#lista=[]
#for y in koncowe:
#    k='%s' %(y)
#    lista.append(k)
#print(' '.join(lista))


print(' '.join(str(y) for y in koncowe))
