import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


data = pd.read_csv('pylearn/csv/housing.csv')
print(data.head())
print(data.describe())
print(data.isnull().sum())

# 1. Pilih hanya kolom yang bertipe angka (integer/float)
numeric_data = data.select_dtypes(include=['number'])

# 2. Hitung korelasi dari data numerik tersebut, lalu buat heatmap-nya
sns.heatmap(numeric_data.corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.show()


# melatih model scikit -learn

x = data[['median_income']]
y = data['median_house_value']

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(x_train, y_train)

# evaluasi model
from sklearn.metrics import mean_squared_error
y_pred = model.predict(x_test)
mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error: {mse}')

# data kategorikal

print("\n--- Hasil Model 2 (Pipeline: Numerik + Kategorikal) ---")
X_full = data[['median_income', 'ocean_proximity']] # Angka + Teks

# Split data
X_train_full, X_test_full, y_train, y_test = train_test_split(X_full, y, test_size=0.2, random_state=42)

categorical_cols = ['ocean_proximity']
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
preprocessor = ColumnTransformer(
    transformers=[
        ('cat', OneHotEncoder(), categorical_cols)
    ],
    remainder='passthrough'
)

from sklearn.pipeline import Pipeline
pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('regressor', LinearRegression())
])

pipeline.fit(X_train_full, y_train)
score = pipeline.score(X_test_full, y_test)
print(f'R^2 Score: {score}')