
list1=[7874018,270]
list2=[5146757,458]
list3=[5281086,121]
list4=[8791,544]
list5=[8246292,399]
list6=[7046589,3875183]
list7=[19037,1174]
list8=[9913079,-3913479]
list9=[9979833,496]
list10=[7786556,-2471804]
list11=[-5707116,-4834005]
list12=[11819,1164]
list13=[7457078,953]
list14=[2535254,-2475191]
list15=[6692196,-4423754]
list16=[9045,1856]
list17=[5307,1760]


listy=[
    [7874018,270],
    [5146757,458],
    [5281086,121],
    [8791,544],
    [8246292,399],
    [7046589,3875183],
    [19037,1174],
    [9913079,-3913479],
    [9979833,496],
    [7786556,-2471804],
    [-5707116,-4834005],
    [11819,1164],
    [7457078,953],
    [2535254,-2475191],
    [6692196,-4423754],
    [9045,1856],
    [5307,1760]
    ]

poz = 0
dlugosc = len(listy)

def dzielenie_wartości(wartosc):
    return round(wartosc[0]/wartosc[1])

while poz < dlugosc:
    print(round(dzielenie_wartości(listy[poz])))
    poz = poz + 1


print (round(list1[0]/list1[1]))
print (round(list2[0]/list2[1]))
print (round(list3[0]/list3[1]))
print (round(list4[0]/list4[1]))
print (round(list5[0]/list5[1]))
print (round(list6[0]/list6[1]))
print (round(list7[0]/list7[1]))
print (round(list8[0]/list8[1]))
print (round(list9[0]/list9[1]))
print (round(list10[0]/list10[1]))
print (round(list11[0]/list11[1]))
print (round(list12[0]/list12[1]))
print (round(list13[0]/list13[1]))
print (round(list14[0]/list14[1]))
print (round(list15[0]/list15[1]))
print (round(list16[0]/list16[1]))
print (round(list17[0]/list17[1]))
