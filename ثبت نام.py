def check_registration_rules(listtest1):
    dicttest1={}
    listtest2,listtest3,listtest4=[],[],[]
    for i in listtest1:
        listtest2=list(i.split('='))
        dicttest1[listtest2[0]]=listtest2[1]
    for i in dicttest1.keys():
        if len(i)>4 and i!="quera" and i!="codecup":
            listtest3.append(i)
    for i in listtest3:
        p=0
        if len(dicttest1[i])>6:
            for j in dicttest1[i]:
                if j.isalpha()==True:
                    p+=1
        if p!=0:
            listtest4.append(i)
    print(listtest4)
check_registration_rules(list(input().split()))