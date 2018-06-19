listy=[
    [798094,249447],
    [112907,344930],
    [600489,327978],
    [919754,358364],
    [988931,777463],
    [550640,477671],
    [969509,217400],
    [278923,722045],
    [478433,553034],
    [304245,654561],
    [741153,933020]
    ]


poz = 0
dlugosc = len(listy)

def suma_argumnetów_listy(argument):
    return (sum(argument))

while poz < dlugosc:
    print(suma_argumnetów_listy(listy[poz]))
    poz = poz +1
