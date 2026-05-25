# summary function dan maps
import pandas as pd

#=================
# summary function
#=================

# describe
df = pd.read_csv('pylearn/csv/data.csv')
print(df.describe())

#mean 
average_age = df['Umur'].mean()
print(f"Rata-rata umur: {average_age}")

#sum
total_age = df['Umur'].sum()
print(f"Total umur: {total_age}")

#min max
min_age = df['Umur'].min()
max_age = df['Umur'].max()
print(f"Umur minimum: {min_age}")
print(f"Umur maksimum: {max_age}")

#value counts
city_counts = df['Kota'].value_counts()
print("Jumlah orang per kota:")
print(city_counts)

# unique
unique_cities = df['Kota'].unique() 
print("Kota unik:", unique_cities)

# head tail
print("5 baris pertama:")
print(df.head())

print("5 baris terakhir:")
print(df.tail())

#=================
# maps
#=================

# map dengan fungsi lambda
df['Umur_10_tahun'] = df['Umur'].map(lambda x: (x * 9/5) + 32)

#apply
df ['difference'] = df.apply(lambda row: row['Umur'] - 30, axis=1)

#fungsi custom map
def categorize_age(age):
    if age < 30:
        return 'Muda'
    elif age < 40:
        return 'Dewasa'
    else:
        return 'Tua'

df['Kategori_Umur'] = df['Umur'].map(categorize_age)

#================================
#fungsi ringkasan dan pemetaan 
#================================

df = pd.read_csv('pylearn/csv/data.csv')
df['umur_category'] = df['Umur'].map(lambda x: 'High' if x > 30 else 'Low')

print(df['umur_category'].value_counts ())
print(df.groupby('umur_category')['Umur'].mean())