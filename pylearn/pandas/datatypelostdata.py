# tipe data dan nilai yang hilang

import pandas as pd

df = pd.read_csv('pylearn/csv/datana.csv')

print(df.dtypes) #menampilkan tipe data setiap kolom

#bersihkan data yang tidak valid
df.replace(['Na', '?', '-'], pd.NA, inplace=True) 

print(df['Usia'].dtype) #menampilkan tipe data kolom 'Usia'

#mengubah tipe data kolom 'Usia' menjadi float
df['Usia'] = df['Usia'].astype(float) 
print(df['Usia'].dtype) 

#mengubah tipe data kolom 'ID Karyawan' menjadi string
df['ID Karyawan'] = df['ID Karyawan'].astype(str) 
print(df['ID Karyawan'].dtype) 

df = df.convert_dtypes() #mengonversi tipe data ke tipe yang lebih sesuaiyy

print("\n--- JUMLAH DATA KOSONG SETELAH REPLASI ---")
print(df.isnull().sum())

# mengisi nilai yang hilang 
#untk kolom katergorikal
df['Departemen'] = df['Departemen'].fillna('Tidak Diketahui') #mengisi nilai yang hilang dengan string 'Tidak Diketahui'

#untuk semua kategorikal
categorical_columns = df.select_dtypes(include=['object']).columns
df[categorical_columns] = df[categorical_columns].fillna('Tidak Diketahui')

#untuk numerik
df['Usia'] = df['Usia'].fillna(df['Usia'].mean()) #mengisi nilai yang hilang dengan rata-rata usia
df['Gaji'] = df['Gaji'].fillna(df['Gaji'].median()) #mengisi nilai yang hilang dengan median gaji

print("\n--- DATA SETELAH DIBERSIHKAN ---")
print(df)
print("\n--- TIPE DATA AKHIR ---")
print(df.dtypes)