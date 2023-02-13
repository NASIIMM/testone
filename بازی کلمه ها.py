import re
def hoora(stringtest):
    listtest1=list(stringtest.split())
    listtest2,listtest3,listtest4=[],[],[]
    print(listtest1)
    for i in listtest1:
        p=0
        for j in i:
            if 65<=ord(j)<=90 or 97<=ord(j)<=122:
                pass
            else:
                p+=1
        if p>=(len(i)/2):
            listtest2.append(i)
    for i in listtest2:
        listtest1.remove(i)
    for i in listtest1:
        print(re.sub("[^A-Za-z]","",i),end=" ")
hoora(input())