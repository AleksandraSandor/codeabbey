dane=[
[746,813,628],
[844,707,2099],
[1122,694,1043],
[1071,744,1236],
[697,817,663],
[540,338,818],
[782,1180,1644],
[1683,481,719],
[926,355,381],
[493,207,197],
[4499,1811,985],
[656,481,1185],
[993,651,2177],
[544,1597,707],
[601,1314,359],
[504,464,344],
[1170,996,1872],
[571,405,1118],
[1389,932,2852],
[142,172,344],
[518,731,441],
[353,1094,509],
[526,394,1163],
[173,184,386]
]

dane = []
liczba_wierszy = int(input())
for x in range(liczba_wierszy):
    wiersz = input()
    lista_liczb_jako_str = wiersz.split(' ')
    
    # 1. sposob
    lista_liczb_jako_int = list(map(int, lista_liczb_jako_str))
    dane.append(lista_liczb_jako_int)
    
    # 2. sposob
    lista_liczb_jako_int = []
    for liczba in lista_liczb_jako_str:
        lista_liczb_jako_int.append(int(liczba))
    dane.append(lista_liczb_jako_int)

print(dane)

for x in dane:
    for n in range(len(x)):
        d = x[:]
        q = d.pop(n)
        if q > sum(d):
            print(0)
            break
    else:
        print(1)
        
    if x[0]>x[1]+x[2]:
        print (0)
    elif x[1]>x[0]+x[2]:
        print (0)
    elif x[2]>x[0]+x[1]:
        print (0)
    else:
        print (1)
    print('--')
        
