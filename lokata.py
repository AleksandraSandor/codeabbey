

print("lokata")

poczatkowy = float(input("podaj swój początkowy stan konta "))
stopa = float(input("podaj roczną stopę oprocentowania w % "))
wiek = float(input("podaj liczbę lat na lokacie "))

print("stan Twojego konta, czyli {:.2f} po {:.0f} lat przy oprocentowaniu {:.2f} % będzie wynosił {:.2f}".format(poczatkowy, wiek, stopa, poczatkowy*(1+(wiek/12))**((stopa/100)*12)))
