dane=[
0.684022200294,
0.35347485682,
0.448962250724,
0.635947724804,
0.160622855183,
0.746222054586,
0.871111270972,
0.340435537975,
0.644412456546,
0.445577757899,
0.45664810529,
0.374926099088,
0.562617554329,
0.416693035513,
0.379756676033,
0.583193659317,
0.156271543819,
0.0339580834843,
0.609942373354,
0.226761240512,
0.1867212574,
0.0796040263958,
0.468765632715,
0.655010554008,
0.0730472649448
]

def f(x):
    return x*6+1
print(' '.join(map(lambda x: x*6+1, dane)))

for x in dane:
    print(int(x*6)+1)
