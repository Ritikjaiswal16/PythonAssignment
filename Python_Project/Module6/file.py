f=open("uk.txt",'w')
inp=list(map(str,input("Enter Some content -: ").strip().split()))

for i in inp:
    f.write('\n')
    f.write(i)
f.close()
f=open("uk.txt",'r')
cont=f.readline()
while cont!='':
    cont=f.readline()
    c=f.readline()
  
    print(cont+c)

cont=f.read()
cont=cont.rstrip('\n')
f.close()
