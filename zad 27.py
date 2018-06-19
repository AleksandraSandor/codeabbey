dane=[]
print ('podaj ilość liczb, które będą przetwarzane :')
ilość=int(input())
print ('podaj liczby, które chcesz modyfikować :')

reply = input()
dane =(reply.split(' '))
dane = list(map(int,dane))
print (dane)

total_swap_count=0
pass_count=0
swap_count=-1

while swap_count != 0:
    poz=0
    swap_count=0
    while poz+1 <len(dane):
        if dane[poz] > dane[poz+1]:
            total_swap_count+=1
            t=dane[poz]
            dane[poz]=dane[poz+1]
            dane[poz+1]=t
            swap_count+=1
        poz+=1
    pass_count+=1
print(dane)
k= "%s %s" %(pass_count, total_swap_count)
print (k)

#reply = input()
#print (reply)
