def fruits(tuplelist1):
    dicttest1,listtest1={},[]
    for i in tuplelist1:
        if i['shape']=='sphere' and 300<=i['mass']<=600 and 100<=i['volume']<=500:
            listtest1.append(i['name'])
    for i in listtest1:
        dicttest1[i]=listtest1.count(i)
    print(dicttest1)
fruit= (
    {'name':'apple', 'shape': 'sphere', 'mass': 350, 'volume': 120},
    {'name':'mango', 'shape': 'square', 'mass': 150, 'volume': 120}, 
    {'name':'lemon', 'shape': 'sphere', 'mass': 300, 'volume': 100},
    {'name':'apple', 'shape': 'sphere', 'mass': 500, 'volume': 250})
fruits(fruit)
