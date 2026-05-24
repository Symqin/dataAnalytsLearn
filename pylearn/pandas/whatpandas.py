# pandas
import pandas as pd

data = { 'Nama' : ['Alice', 'Bob', 'Charlie', 'David'],
         'Umur' : [25, 30, 35, 40],
         'Kota' : ['New York', 'Los Angeles', 'Chicago', 'Houston'] }

df = pd.DataFrame(data)
print(df)

# Menyimpan DataFrame ke file CSV
df.to_csv('data.csv', index=False)

# Membaca DataFrame dari file CSV
dataindus = pd.read_csv('industry.csv')
print(dataindus.head())

#modfifikasi data
df.set_index('Nama', inplace=True)
print(df)

# pemilihan kolom
print(df['Umur'])

# pemilihan baris
print(df.loc['Alice'])

# filtering kondisional
filtered_df = df[df['Umur'] > 30]
print(filtered_df)

# menambahkan dan modifikasi data
df['Pekerjaan'] = ['Engineer', 'Doctor', 'Artist', 'Lawyer']
print(df)

# menghapus kolom
df.drop('Kota', axis=1, inplace=True)

# menghapus baris
df.drop('Bob', axis=0, inplace=True)

# menganti nilai
df.at['Charlie', 'Umur'] = 36
print(df)


