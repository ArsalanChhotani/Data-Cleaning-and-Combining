import pandas as pd


df1 = pd.read_csv('E:\\DS\\data1.csv', index_col = 0)
df2 = pd.read_csv('E:\\DS\\data2.csv', index_col = 1)

print(df1)
print(df2)

df3 = pd.concat([df1,df2] , ignore_index = True)
print(df3)

df4 = pd.read_csv('E:\\DS\\data3.csv',index_col = 0)
print(df4)

df5 = df3.join(df4)
print(df5)

df6 = pd.read_json('E:\\DS\\data.json')
print(df6)

df7 = pd.concat([df5,df6],ignore_index = True)
print(df7)


df7 = df7.convert_objects(convert_numeric = True)
df7 = df7.fillna(df7.mean())
print(df7)
