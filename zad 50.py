
napis = "Was it a cat I saw?"
print(napis)

k=list(napis)
print (k)
for x in k:
    if x == ",":
        k.remove(x)
    elif x == "-":
        k.remove(x)
    elif x == "!":
        k.remove(x)    
    elif x == " ":
        k.remove(x)
    elif x == "?":
        k.remove(x)
for x in k:
    if x ==" ":
        k.remove(x)
b= ''.join(k)
print(b)
print (b.isalpha())
y=b.lower()
print(y)

z=y[::-1]
print(z)
if y == z:
    print ("Y")
else:
    print ("N")
