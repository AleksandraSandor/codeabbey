dane=[45733,631,7875,268,33127,22,241,5697,397,3714,4174,28948,36,4130,2459,35372,270,16312]

steps=0

for x in dane:
    steps=0
    while x>1:
        if x%2==0:
            x=x/2
        else:
            x=x*3+1
        steps+=1
    print(steps)


    
    

