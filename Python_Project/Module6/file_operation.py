def check_file(name):
    flist=open("list.txt",'r')
    line=flist.readline()
    while line!='':
        if str(line)==str(name):
            return False
        line=flist.readline()
    flist.close()
    return True
fname=input("Enter File Name with extension -: ")
if check_file(fname):
    print("File Doesnot Exist")
    f=open(fname,'w')
    f.close()
    f=open("list.txt",'a')
    f.write(fname)
    print("New file Created with name as = ",fname)
else:
    print("File Found")

print("1.Read")
print("2.Write")
print("3.Append")
i=int(input("Choose one Option Index -: "))
if i==1:
    fopen=open(str(fname),'r')
    line=fopen.readline()
    while line!='':
        print(line)
        line=fopen.readline()
    fopen.close()
elif i==3:
    fopen=open(str(fname),'a')
    obj=input("Enter Content -: ")
    fopen.write(obj)
    fopen.close()
elif i==2:
    fopen=open(str(fname),'w')
    obj=input("Enter Content -: ")
    fopen.write(obj)
    fopen.close()
