import pandas as pd
squad={'batsman':{'Rohit':{'Matches':224,'run':9115,'high':264},
                  'virat':{'Matches':245,'run':11792,'high':183},
                  'sachin':{'Matches':463,'run':18426,'high':200}}}
df=pd.DataFrame(squad['batsman'])
print(df)
