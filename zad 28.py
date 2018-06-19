#BMI = weight/height^2
#under <18.5
#normal 18.5<=BMI<25.0
#over 25.0<=BMI<30.0
#obese 30.0<=BMI

lista0=[92,2.56]
lista1=[118,2.02]
lista2=[82,1.49]
lista3=[112,1.84]
lista4=[68,1.72]
lista5=[92,2.14]
lista6=[65,1.40]
lista7=[82,1.65]
lista8=[85,2.24]
lista9=[104,3.07]
lista10=[85,2.17]
lista11=[99,2.57]
lista12=[63,1.30]
lista13=[57,1.73]
lista14=[61,1.56]
lista15=[57,1.28]
lista16=[94,2.50]
lista17=[87,2.33]
lista18=[52,1.47]
lista19=[43,1.34]
lista20=[116,2.00]
lista21=[109,2.53]
lista22=[82,1.98]
lista23=[117,3.00]
lista24=[90,1.70]
lista25=[48,1.73]
lista26=[43,1.14]
lista27=[67,1.83]
lista28=[107,2.03]
lista29=[92,2.66]
lista30=[47,1.18]
lista31=[40,1.14]
lista32=[44,1.30]
lista33=[118,2.72]

listy = [
    [92,2.56],
    [118,2.02],
    [82,1.49],
    [112,1.84],
    [68,1.72],
    [92,2.14],
    [65,1.40],
    [82,1.65],
    [85,2.24],
    [104,3.07],
    [85,2.17],
    [99,2.57],
    [63,1.30],
    [57,1.73],
    [61,1.56],
    [57,1.28],
    [94,2.50],
    [87,2.33],
    [52,1.47],
    [43,1.34],
    [116,2.00],
    [109,2.53],
    [82,1.98],
    [117,3.00],
    [90,1.70],
    [48,1.73],
    [43,1.14],
    [67,1.83],
    [107,2.03],
    [92,2.66],
    [47,1.18],
    [40,1.14],
    [44,1.30],
    [118,2.72]
    ]

poz = 0

def BMI(wartosc):
    return round(wartosc[0]/(wartosc[1]**2))

while poz < len(listy):
    
    if (round(BMI(listy[poz]))) >= 30.0:
        print ("obese")
    elif(round(BMI(listy[poz]))) >= 25.0:
        print ("over")
    elif(round(BMI(listy[poz]))) >= 18.5:
        print ("normal")
    else:
        print ("under")
    poz = poz + 1



print("ola")

BMI0=(lista0[0]/(lista0[1]**2))
BMI1=(lista1[0]/(lista1[1]**2))
BMI2=(lista2[0]/(lista2[1]**2))
BMI3=(lista3[0]/(lista3[1]**2))
BMI4=(lista4[0]/(lista4[1]**2))
BMI5=(lista5[0]/(lista5[1]**2))
BMI6=(lista6[0]/(lista6[1]**2))
BMI7=(lista7[0]/(lista7[1]**2))
BMI8=(lista8[0]/(lista8[1]**2))
BMI9=(lista9[0]/(lista9[1]**2))
BMI10=(lista10[0]/(lista10[1]**2))
BMI11=(lista11[0]/(lista11[1]**2))
BMI12=(lista12[0]/(lista12[1]**2))
BMI13=(lista13[0]/(lista13[1]**2))
BMI14=(lista14[0]/(lista14[1]**2))
BMI15=(lista15[0]/(lista15[1]**2))
BMI16=(lista16[0]/(lista16[1]**2))
BMI17=(lista17[0]/(lista17[1]**2))
BMI18=(lista18[0]/(lista18[1]**2))
BMI19=(lista19[0]/(lista19[1]**2))
BMI20=(lista20[0]/(lista20[1]**2))
BMI21=(lista21[0]/(lista21[1]**2))
BMI22=(lista22[0]/(lista22[1]**2))
BMI23=(lista23[0]/(lista23[1]**2))
BMI24=(lista24[0]/(lista24[1]**2))
BMI25=(lista25[0]/(lista25[1]**2))
BMI26=(lista26[0]/(lista26[1]**2))
BMI27=(lista27[0]/(lista27[1]**2))
BMI28=(lista28[0]/(lista28[1]**2))
BMI29=(lista29[0]/(lista29[1]**2))
BMI30=(lista30[0]/(lista30[1]**2))
BMI31=(lista31[0]/(lista31[1]**2))
BMI32=(lista32[0]/(lista32[1]**2))
BMI33=(lista33[0]/(lista33[1]**2))


if BMI0 < 18.5:
    print ("under")
elif 18.5<=BMI0<25.0:
    print ("normal")
elif 25.0<=BMI0<30.0:
    print ("over")
elif BMI0>=30.0:
    print("obese")
if BMI1 < 18.5:
    print ("under")
elif 18.5<=BMI1<25.0:
    print ("normal")
elif 25.0<=BMI1<30.0:
    print ("over")
elif BMI1>=30.0:
    print("obese")
if BMI2 < 18.5:
    print ("under")
elif 18.5<=BMI2<25.0:
    print ("normal")
elif 25.0<=BMI2<30.0:
    print ("over")
elif BMI2>=30.0:
    print("obese")
if BMI3 < 18.5:
    print ("under")
elif 18.5<=BMI3<25.0:
    print ("normal")
elif 25.0<=BMI3<30.0:
    print ("over")
elif BMI3>=30.0:
    print("obese")
if BMI4 < 18.5:
    print ("under")
elif 18.5<=BMI4<25.0:
    print ("normal")
elif 25.0<=BMI4<30.0:
    print ("over")
elif BMI4>=30.0:
    print("obese")
if BMI5 < 18.5:
    print ("under")
elif 18.5<=BMI5<25.0:
    print ("normal")
elif 25.0<=BMI5<30.0:
    print ("over")
elif BMI5>=30.0:
    print("obese")
if BMI6 < 18.5:
    print ("under")
elif 18.5<=BMI6<25.0:
    print ("normal")
elif 25.0<=BMI6<30.0:
    print ("over")
elif BMI6>=30.0:
    print("obese")
if BMI7 < 18.5:
    print ("under")
elif 18.5<=BMI7<25.0:
    print ("normal")
elif 25.0<=BMI7<30.0:
    print ("over")
elif BMI7>=30.0:
    print("obese")
if BMI8 < 18.5:
    print ("under")
elif 18.5<=BMI8<25.0:
    print ("normal")
elif 25.0<=BMI8<30.0:
    print ("over")
elif BMI8>=30.0:
    print("obese")
if BMI9 < 18.5:
    print ("under")
elif 18.5<=BMI9<25.0:
    print ("normal")
elif 25.0<=BMI9<30.0:
    print ("over")
elif BMI9>=30.0:
    print("obese")
if BMI10 < 18.5:
    print ("under")
elif 18.5<=BMI10<25.0:
    print ("normal")
elif 25.0<=BMI10<30.0:
    print ("over")
elif BMI10>=30.0:
    print("obese")
if BMI11 < 18.5:
    print ("under")
elif 18.5<=BMI11<25.0:
    print ("normal")
elif 25.0<=BMI11<30.0:
    print ("over")
elif BMI11>=30.0:
    print("obese")
if BMI12 < 18.5:
    print ("under")
elif 18.5<=BMI12<25.0:
    print ("normal")
elif 25.0<=BMI12<30.0:
    print ("over")
elif BMI12>=30.0:
    print("obese")
if BMI13 < 18.5:
    print ("under")
elif 18.5<=BMI13<25.0:
    print ("normal")
elif 25.0<=BMI13<30.0:
    print ("over")
elif BMI13>=30.0:
    print("obese")
if BMI14 < 18.5:
    print ("under")
elif 18.5<=BMI14<25.0:
    print ("normal")
elif 25.0<=BMI14<30.0:
    print ("over")
elif BMI14>=30.0:
    print("obese")
if BMI15 < 18.5:
    print ("under")
elif 18.5<=BMI15<25.0:
    print ("normal")
elif 25.0<=BMI15<30.0:
    print ("over")
elif BMI15>=30.0:
    print("obese")
if BMI16 < 18.5:
    print ("under")
elif 18.5<=BMI16<25.0:
    print ("normal")
elif 25.0<=BMI16<30.0:
    print ("over")
elif BMI16>=30.0:
    print("obese")
if BMI17 < 18.5:
    print ("under")
elif 18.5<=BMI17<25.0:
    print ("normal")
elif 25.0<=BMI17<30.0:
    print ("over")
elif BMI17>=30.0:
    print("obese")
if BMI18 < 18.5:
    print ("under")
elif 18.5<=BMI18<25.0:
    print ("normal")
elif 25.0<=BMI18<30.0:
    print ("over")
elif BMI18>=30.0:
    print("obese")
if BMI19 < 18.5:
    print ("under")
elif 18.5<=BMI19<25.0:
    print ("normal")
elif 25.0<=BMI19<30.0:
    print ("over")
elif BMI19>=30.0:
    print("obese")
if BMI20 < 18.5:
    print ("under")
elif 18.5<=BMI20<25.0:
    print ("normal")
elif 25.0<=BMI20<30.0:
    print ("over")
elif BMI20>=30.0:
    print("obese")
if BMI21 < 18.5:
    print ("under")
elif 18.5<=BMI21<25.0:
    print ("normal")
elif 25.0<=BMI21<30.0:
    print ("over")
elif BMI21>=30.0:
    print("obese")
if BMI22 < 18.5:
    print ("under")
elif 18.5<=BMI22<25.0:
    print ("normal")
elif 25.0<=BMI22<30.0:
    print ("over")
elif BMI22>=30.0:
    print("obese")
if BMI23 < 18.5:
    print ("under")
elif 18.5<=BMI23<25.0:
    print ("normal")
elif 25.0<=BMI23<30.0:
    print ("over")
elif BMI23>=30.0:
    print("obese")
if BMI24 < 18.5:
    print ("under")
elif 18.5<=BMI24<25.0:
    print ("normal")
elif 25.0<=BMI24<30.0:
    print ("over")
elif BMI24>=30.0:
    print("obese")
if BMI25 < 18.5:
    print ("under")
elif 18.5<=BMI25<25.0:
    print ("normal")
elif 25.0<=BMI25<30.0:
    print ("over")
elif BMI25>=30.0:
    print("obese")
if BMI26 < 18.5:
    print ("under")
elif 18.5<=BMI26<25.0:
    print ("normal")
elif 25.0<=BMI26<30.0:
    print ("over")
elif BMI26>=30.0:
    print("obese")
if BMI27 < 18.5:
    print ("under")
elif 18.5<=BMI27<25.0:
    print ("normal")
elif 25.0<=BMI27<30.0:
    print ("over")
elif BMI27>=30.0:
    print("obese")
if BMI28 < 18.5:
    print ("under")
elif 18.5<=BMI28<25.0:
    print ("normal")
elif 25.0<=BMI28<30.0:
    print ("over")
elif BMI28>=30.0:
    print("obese")
if BMI29 < 18.5:
    print ("under")
elif 18.5<=BMI29<25.0:
    print ("normal")
elif 25.0<=BMI29<30.0:
    print ("over")
elif BMI29>=30.0:
    print("obese")
if BMI30 < 18.5:
    print ("under")
elif 18.5<=BMI30<25.0:
    print ("normal")
elif 25.0<=BMI30<30.0:
    print ("over")
elif BMI30>=30.0:
    print("obese")
if BMI31 < 18.5:
    print ("under")
elif 18.5<=BMI31<25.0:
    print ("normal")
elif 25.0<=BMI31<30.0:
    print ("over")
elif BMI31>=30.0:
    print("obese")
if BMI32 < 18.5:
    print ("under")
elif 18.5<=BMI32<25.0:
    print ("normal")
elif 25.0<=BMI32<30.0:
    print ("over")
elif BMI32>=30.0:
    print("obese")
if BMI33 < 18.5:
    print ("under")
elif 18.5<=BMI33<25.0:
    print ("normal")
elif 25.0<=BMI33<30.0:
    print ("over")
elif BMI33>=30.0:
    print("obese")
