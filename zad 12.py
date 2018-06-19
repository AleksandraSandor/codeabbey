dane=[
[12,4,39,4,29,13,4,13],
[9,17,31,6,14,1,31,5],
[1,22,26,35,20,8,13,33],
[1,15,53,11,13,11,14,49],
[22,9,1,59,25,23,40,59],
[5,21,39,25,9,16,53,12],
[16,18,2,45,18,22,44,23],
[14,17,38,52,27,4,34,23],
[16,8,17,30,28,3,12,36],
[5,13,23,57,10,3,7,54],
[22,17,27,43,26,4,43,50],
[10,11,9,11,28,14,3,50],
[7,10,40,25,15,7,55,50],
[21,16,5,32,27,3,22,17],
[23,15,50,34,29,5,49,4],
]

poz=0
for lista in dane:
    roznica_czasu=(((lista[poz+4]*24*60*60+lista[poz+5]*60*60+lista[poz+6]*60+lista[poz+7])-(lista[poz]*24*60*60+lista[poz+1]*60*60+lista[poz+2]*60+lista[poz+3])))
    days=(roznica_czasu-(roznica_czasu%(24*60*60)))/(24*60*60)
    hours=(roznica_czasu-(days*24*60*60)-((roznica_czasu-(days*24*60*60))%(60*60)))/(60*60)
    minutes=(((roznica_czasu-(days*24*60*60)-(hours*60*60)-((roznica_czasu-(days*24*60*60)-(hours*60*60))%(60)))/(60)))
    seconds=(((roznica_czasu-(days*24*60*60)-(hours*60*60)-(minutes*60))))
    days=str(round(days))
    hours=str(round(hours))
    minutes=str(round(minutes))
    seconds=str(round(seconds))
    
    print ("("+days+" "+hours+" "+minutes+" "+seconds+")")
