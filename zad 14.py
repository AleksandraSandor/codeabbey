dane = []
lista=[]
print ('podaj liczbę która chcesz przetworzyć :')
przetwarzana_liczba=int(input())
print ('podaj działania, które chcesz wykonać na liczbie', przetwarzana_liczba , 'w kolejności: działanie i liczba :')

    
while True:
    reply = input()
    if reply == '': break
    dane = (reply.split(' '))
    #print (dane)
    lista.append(dane)
print(lista)

    
for x in lista:
    if x[0] == '*':
        przetwarzana_liczba*=int(x[1])
    elif x[0] == '+':
        przetwarzana_liczba+=int(x[1])
    elif x[0] == '%':
        przetwarzana_liczba%=int(x[1])
    else:
        print ('błąd')
print (przetwarzana_liczba)

        

    
#operator w bibliotece standardowej -funkcja - słownik (* - operator mnożenie)


