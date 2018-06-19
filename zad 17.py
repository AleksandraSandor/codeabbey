dane=[3,1,4,1,5,9]
poz = 0
dlugosc = len(dane)
accumulator = 0
limit = 10000007
seed = 113

for number in dane:
    accumulator += number * (seed ** dlugosc)
    dlugosc -= 1
print (accumulator%limit)

while poz<len(dane):
    accumulator += dane[poz]*(seed**dlugosc)
    poz+=1
    dlugosc-=1
print (accumulator%limit)




#result = 0

#result = (result + a[0]) * seed = (0 + 3) * 113 = 339

#result = (result + a[1]) * seed = (339 + 1) * 113 = 38420

#result = (result + a[2]) * seed = (38420 + 4) * 113 = 4341912

#result = (result + a[3]) * seed = (4341912 + 1) * 113 = 490636169
#result = result % limit = 490636169 % 10000007 = 635826

#result = (result + a[4]) * seed = (635826 + 5) * 113 = 71848903
#result = result % limit = 71851163 % 10000007 = 1848854

#result = (result + a[5]) * seed = (1848854 + 9) * 113 = 208921519
#result = result % limit = 209176899 % 10000007 = 8921379

print (243643962926468 % 10000007)
