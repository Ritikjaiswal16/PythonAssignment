import pickle
i=int(input("Enter 1 for read and 2 for write"))
if i==1:
    in_file=open('uk.txt','rb')
    pb=pickle.load(in_file)
    in_file.close()
    print(pb)
if i==2:
    file=open('uk.txt','wb')
    re=list(map(str,input("Write Content -: ").strip().split()))
    pb=pickle.dump(re,file)
    file.close()
