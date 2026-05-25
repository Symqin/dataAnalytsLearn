# penamaan dan penggabungan 
import pandas as pd

#menggunakan metode rename
data = {"A": [1, 2, 3], "B": [4, 5, 6], "C": [7, 8, 9]}
df = pd.DataFrame(data)
df.rename(columns={"A": "Alpha", "B": "Beta"}, inplace=True)
print(df)

# menggunakan atribut columns
df.columns = ['Alpha', 'Beta', 'Gamma']
print(df)

# menggabungkan DataFrame dengan concat
df1 = pd.DataFrame({'Nama': ['Alice', 'Bob'], 'Umur': [25, 30]})
df2 = pd.DataFrame({'Nama': ['Charlie', 'David'], 'Umur': [35, 40]})
df_concat = pd.concat([df1, df2], axis=0)
print(df_concat)

# menggabungkan DataFrame dengan merge
df_left = pd.DataFrame({'ID': [1, 2, 3], 'Nama': ['Alice', 'Bob', 'Charlie']})
df_right = pd.DataFrame({'ID': [2, 3, 4], 'Kota': ['New York', 'Los Angeles', 'Chicago']})
df_merge = pd.merge(df_left, df_right, on='ID', how='inner') # inner join berdasarkan kolom 'ID' (irisan)
print(df_merge)

# menggabungkan DataFrame dengan join
df_1 = pd.DataFrame({"A": [1, 2]}, index=["K1", "K2"])
df_2 = pd.DataFrame({"B": [3, 4]}, index=["K1", "K2"])

result = df_1.join(df_2, how="inner")
print(result)