# Grouping dan sort
import pandas as pd

# ==========================================
# PERSIAPAN: Memuat Dataset
# ==========================================
df = pd.read_csv('pylearn/csv/sales_data.csv')
print("--- DATA AWAL ---")
print(df.head(), "\n")

# ==========================================
# BAGIAN 1: GROUPING (Pengelompokan)
# ==========================================

# 1. Grouping dengan satu agregasi
grouped = df.groupby('Wilayah')['Penjualan'].agg(['sum', 'mean'])
print("--- GROUPING: Wilayah (Sum & Mean) ---")
print(grouped, "\n")

# 2. Grouping Multi-Level (Berdasarkan lebih dari satu kolom)
multi_grouped = df.groupby(['Wilayah', 'Kategori_Produk'])['Penjualan'].agg(['sum', 'mean'])
print("--- GROUPING MULTI-LEVEL: Wilayah & Kategori ---")
print(multi_grouped, "\n")

# 3. Reset Index (Mengembalikan index menjadi kolom biasa)
reset_grouped = multi_grouped.reset_index()
print("--- RESET INDEX DARI MULTI-GROUPED ---")
print(reset_grouped.head(), "\n")

# 4. Grouping dengan Named Aggregation (Memberi nama kolom baru)
grouped_named = df.groupby('Wilayah').agg(
    Total_Penjualan=('Penjualan', 'sum'),
    Rata_Rata=('Penjualan', 'mean'),
    Jumlah_Trx=('Penjualan', 'count')
)
print("--- GROUPING DENGAN NAMA KOLOM KUSTOM ---")
print(grouped_named, "\n")


# ==========================================
# BAGIAN 2: SORTING (Pengurutan)
# ==========================================

# 1. Pengurutan Dasar (Menurun/Descending)
sorted_df = df.sort_values(by='Penjualan', ascending=False)
print("--- SORTING: Penjualan Tertinggi ke Terendah ---")
print(sorted_df.head(), "\n")

# 2. Pengurutan Berdasarkan Beberapa Kolom (Wilayah Naik, Penjualan Turun)
multi_sorted = df.sort_values(by=['Wilayah', 'Penjualan'], ascending=[True, False])
print("--- SORTING MULTIPLE: Wilayah (A-Z) & Penjualan (Tinggi-Rendah) ---")
print(multi_sorted.head(), "\n")

# 3. Sorting pada Index (sort_index)
grouped_for_index = df.groupby(['Wilayah', 'Kategori_Produk'])['Penjualan'].sum()
sorted_index = grouped_for_index.sort_index()
print("--- SORTING BERDASARKAN INDEX ---")
print(sorted_index, "\n")


# ==========================================
# BAGIAN 3: MENGGABUNGKAN GROUPING & SORTING
# ==========================================

# Mencari 5 Wilayah Teratas Berdasarkan Total Penjualan
grouped_sales = df.groupby('Wilayah')['Penjualan'].agg(['sum'])
sorted_sales = grouped_sales.sort_values(by='sum', ascending=False)
top_regions = sorted_sales.head(5)

print("--- 5 WILAYAH TERATAS BERDASARKAN TOTAL PENJUALAN ---")
print(top_regions)