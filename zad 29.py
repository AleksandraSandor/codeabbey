dane=[]
print ('podaj ilość liczb, które będą przetwarzane :')
ilość=int(input())
print ('podaj liczby, które chcesz modyfikować :')

reply = input()
dane =(reply.split(' '))
dane = list(map(int,dane))
print (dane)

counter_list=list(enumerate(dane,1))
print (counter_list)
counter_list.sort(key=lambda x: x[1])
print (counter_list)

#lista=[]
#for y in counter_list:
#    k='%s' %(y[0])
#    lista.append(k)

#print(' '.join(lista))

print(' '.join(str(y[0]) for y in counter_list))
