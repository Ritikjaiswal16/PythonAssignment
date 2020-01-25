import pandas as pd
fruits={'apple':{'major_producer':'China','carbo':13.81,'fat':0.17,'protein':0.26},
                 'banana':{'major_producer':'Indonesia','carbo':11.06,'fat':0.26,'protein':0.34},
                 'mango':{'major_producer':'India','carbo':25.45,'fat':0.19,'protein':0.28}}
d=pd.DataFrame(fruits)
print(d)
max=0.0
for i in d.keys():
    j=d[i].get('protein')
    if j >max:
        max=j
print( 'maximum protien',max)
