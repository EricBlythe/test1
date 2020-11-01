import time
print('COPYRIGHT RESERVED\n')
i=0
t=time.time()
try:
    fr=open('Prime Numbers.txt','r')
    P=[]
    for line in fr:
        line=int(line)
        P.append(line)
    fr.close()
except:
    P=[2,3]
    fw=open('Prime Numbers.txt','w')
    for p in P:
        p=str(p)
        fw.write(p+'\n')
    fw.close()
N=P[-1]
while True:
    N=N+2
    d=1+N**0.5
    for p in P:
        if p>d or p==P[-1]:
            P.append(N)
            f=open('Prime Numbers.txt','a')
            f.write(str(N)+'\n')
            f.close()
            i=i+1
            if time.time()-t>=5:
                print(i)
                t=time.time()
                i=0
            break
        if N%p==0:
            break
    

