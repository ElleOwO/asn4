#LYIN MYA
#LYM284
#11192838
#COM145
#SECTION04

import Statistics as Stat

testing_add = [
    {'inputs' : [0],    
     'outputs':[1, 0],    
     'reason' : 'No change to avg'},

    {'inputs' : [1],    
     'outputs':[1, 1], 
     'reason' : 'Positive value'},

    {'inputs' : [-5],    
     'outputs':[1, -5], 
     'reason' : 'Negative value'},

    {'inputs' : [4.4],   
     'outputs':[1, 4.4],
     'reason' : 'Floating point positive value'},

    {'inputs' : [-10.2],    
     'outputs':[1, -10.2], 
     'reason' : 'Floating point negative value'},
]

for i in testing_add:
    calculated = i['inputs']
    expected = i['outputs']

   
    Stats_adt = Stat.create()


    Stat.add(Stats_adt, args_in[0])

    # checking count
    if Stats_adt['count'] != expected[0]:
        print('error in add(): expected count', expected[0],
              ' but found ', thing['count'], '--', i['reason'])

    # check the ave
    if thing['avg'] != expected[1]:
        print('error in add(): expected avg', expected[1],
              ' but found ', thing['avg'], '--', i['reason'])
