dane=[
[4511,292,6182,198,4981,13270, 0],
[1979,1749,1475,544,604,1073,1472,1358],
[895,764,763,738,433,248,270],
[224,832,1125,81,1396,1161,854,1420],
[13,159,99,450,16,235,89,284,91,428,398,265,363,268],
[1936,1028,1418,527,1954,1642,1358],
[2819,570,2110,306,7704,3968,502,2047,5545,7690],
[29,214,80,243,156,212,168,34],
[20,151,199,86,139]
]

poz = 0

for x in dane:
    k = len(x)
    print (round((sum(x))/k))