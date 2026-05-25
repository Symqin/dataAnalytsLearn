# indeksisasi , pemilihan dan penugasan 

import pandas as pd

data = { 'Nama' : ['Alice', 'Bob', 'Charlie', 'David'],
         'Umur' : [25, 30, 35, 40]}

df = pd.DataFrame(data, index=['orang1', 'orang2', 'orang3', 'orang4'])
print(df)

#=================
#indexing 
#=================

# indeks label loc
print(df.loc['orang1', 'Umur'])

# indeks posisi iloc
print(df.iloc[1, 0])

# indeks campuran
print(df.iloc[1]['Umur'])

#=================
# memilih data 
#=================

usia = df['Umur']
subset = df[['Nama', 'Umur']]

fitered_df = df[df['Umur'] > 30]
print(fitered_df)

filtered_df = df[df['Nama'].str.startswith('A')]
print(filtered_df)

filtered_df = df[df['Umur'].notnull()]
print(filtered_df)

#==============
# assigning
#==============
# Modifikasi nilai dengan loc
df.loc['orang1', 'Umur'] = 32

df['kota'] = ['New York', 'Los Angeles', 'Chicago', 'Houston']

#mengganti nilai dengan replace
df['kota'] = df['kota'].replace('New York', 'NYC')
print(df)

#menetapkan ulang index
df.set_index('Nama', inplace=True)
print(df)

#mengubah urutan baris
df = df.iloc[::-1].reset_index(drop=True)
print(df)

#=================
# lanjutkan 
#=================

array = [['A','A','B','B'], [1,2,3,4]]

index = pd.MultiIndex.from_arrays(array, names=['Huruf', 'Nomor'])
df_multi = pd.DataFrame({'Nilai': [10, 20, 30, 40]}, index=index)
print(df_multi)