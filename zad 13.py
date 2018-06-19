dane=[698048,1816452,2732,443237627,100,260,161544268,1270,1771345,6722,288407274,85086070,86,419197,28,1621838,52,72,2,5091,43,16426223,10546830,68,4972424,2771,8,361157309,325842382,1,27022,22357505,5,77,78,88644090,409,2778,21]
poz = 0

accumulator = 0


while poz < len(dane):
    d = x = int(dane[poz])
    n=(len(str(dane[poz])))
    divider=1
    accumulator=0
    while n:
        x = (((d // divider) % 10)*n)
        accumulator += x
        divider *= 10
        n-=1
    print (accumulator)
    poz=poz+1




