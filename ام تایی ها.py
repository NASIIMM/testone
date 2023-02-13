def calculator(len1,part1,listtest1):
    p=0
    t,sum2,sum=0,0,0
    for j in range(len1//part1):
        listtest2=[]
        sum=0
        t+=1
        for i in range(part1):
            listtest2.append(listtest1[p])
            p+=1
        for i in listtest2:
            sum+=int(i)
        if t%2==0:
            sum2+=sum
        if t%2!=0 and t!=1:
            sum2-=sum
        if t==1:
            sum2=sum
    if (len(listtest1)-p-1)!=0:
        listtest2=[] 
        sum=0
        for i in range(len(listtest1)-p):
            listtest2.append(listtest1[p])
            p+=1
        for i in listtest2:
            sum+=int(i)
        if (t+1)%2==0:
            sum2+=sum
        if (t+1)%2!=0 and t!=1:
            sum2-=sum
        if (t+1)==1:
            sum2=sum
    print(sum2)
calculator(int(input()),int(input()),list(input().split()))
        
