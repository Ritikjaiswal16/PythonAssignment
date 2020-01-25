d={1:{'name':'John','age':'27','sex':'Male'},
   2:{'name':'Marie','age':'22','sex':'Female'}}

print(d)
d[3]={}
d[3]['name']='Luna'
d[3]['age']='24'
d[3]['sex']='Female'
d[3]['Married']='No'
for i in range(1,4):
    del d[i]['sex']
for key in d:
    print(key)
for i in d:
    print(i," ",d[i])
    
    
