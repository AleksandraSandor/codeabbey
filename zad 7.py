
numbers=[325,279,35,475,483,588,106,530,333,574,571,505,306,304,272,499,405,126,556,264,184,137,331,228,73,208,200,463,89,479,275,382,157,279,257,39,267]
poz = 0
dlugosc = len(numbers)

def convert_farenheit_to_celcius(farenheit):
    return round((farenheit-32)/1.8)



while poz < dlugosc:
    print(convert_farenheit_to_celcius(numbers[poz]))
    poz = poz + 1

for x in numbers:
    print(convert_farenheit_to_celcius(x))


while poz < dlugosc:
    print(round((((numbers[poz]-32)/1.8))))
    poz = poz + 1

for x in numbers:
    print(round((((x-32)/1.8))))
