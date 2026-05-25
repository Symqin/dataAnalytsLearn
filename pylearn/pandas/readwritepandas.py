# read and write and modify data with pandas
import os
import pandas as pd

data = { 'Nama' : ['Alice', 'Bob', 'Charlie', 'David'],
         'Umur' : [25, 30, 35, 40],
         'Kota' : ['New York', 'Los Angeles', 'Chicago', 'Houston'] }

df = pd.DataFrame(data)
print(df)

# series
usia_series = df['Umur']
print(usia_series)

# index
df = pd.DataFrame(data, index=['orang1', 'orang2', 'orang3', 'orang4'])
print(df)

# read csv
df_from_csv = pd.read_csv('industry.csv')
print(df_from_csv)

# shape and head
print(df_from_csv.shape)
print(df_from_csv.head())

# write csv
df.to_csv('new.csv', index=False)

# read file from different path
df_from_csv = pd.read_csv('pylearn/new.csv')
print(df_from_csv)

# mengubah direktori kerja
os.chdir('pylearn')
df_from_csv = pd.read_csv('new.csv')
print(df_from_csv)

#path dinamis

data_directory = os.getenv('DATA_DIR', 'C:\\Users\\mutaq\\Documents\\code\\dataAnalytsLearn')
file_path = os.path.join(data_directory, 'industry.csv')
df_from_csv = pd.read_csv(file_path)
print(df_from_csv.head())

#url csv
url = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv'
df_from_url = pd.read_csv(url)  
print(df_from_url.head())

# implementasi read dan write csv dengan pandas
# Membuat DataFrame baru

new_data = { 
    'product': ['Laptop', 'Smartphone', 'Tablet', 'Headphones'],
    'price': [1200, 800, 400, 150],
    'stock': [10, 25, 15, 50]
}

new_df = pd.DataFrame(new_data , index=['item1', 'item2', 'item3', 'item4'])
print(new_df)

# akses series
price_series = new_df['price']
print(price_series)

# memeriksa dimensi DataFrame
print(new_df.shape)

# menampilkan beberapa baris pertama
print(new_df.head(3))

