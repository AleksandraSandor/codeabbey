dane=[]
print ('podaj liczby, które chcesz modyfikować :')
reply = input()
dane =(reply.split(' '))
dane = list(map(int,dane))
dane.pop(-1)

pass_count=0
swap_count=-1

poz=0
swap_count=0
while poz+1 <len(dane):
    if dane[poz] > dane[poz+1]:
        t=dane[poz]
        dane[poz]=dane[poz+1]
        dane[poz+1]=t
        swap_count+=1
    poz+=1
    pass_count+=1

#obliczanie sumy kontrolnej

multiple = 113
modulo = 10000007
checksum = 0
for number in dane:
    number = int(number)

    checksum += number
    checksum *= multiple
    checksum = checksum % modulo

w="%s %s" %(swap_count, checksum)
print (w)
