# hyperparameter adalah sebuah parameter yang digunakan untuk mengontrol proses pelatihan model machine learning. 
# Hyperparameter tidak dipelajari dari data, tetapi ditentukan sebelum proses pelatihan dimulai. 
# Contoh hyperparameter termasuk tingkat pembelajaran (learning rate), jumlah pohon dalam random forest, atau jumlah lapisan dalam jaringan saraf.

from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor
from sklearn.model_selection import cross_val_score
from sklearn.datasets import make_regression, load_breast_cancer

x, y = make_regression(n_samples=100, n_features=1, noise=0.1, random_state=42)

# penyempurnaan hyperparameter
#--------------------------------------------
# menyesuaikan max_depth pada decision tree
#-------------------------------------------
for depth in [3,5,10]:
    model = DecisionTreeRegressor(max_depth=depth)
    score = cross_val_score(model, x, y, cv=5)
    print(f'Max Depth: {depth}, Mean CV Score: {score.mean()}')

#--------------------------------------------
# permintaan sewa sepeda(manual tuning)
#--------------------------------------------
print("--- Studi Kasus 1: Penyempurnaan Manual ---")

X_sepeda, y_sepeda = make_regression(n_samples=500, n_features=3, noise=15, random_state=42)

kedalaman_yang_diuji = [2,3,5,7,10,15]

skor_terbaik = -float('inf')
kedalaman_terbaik = None

for kedalaman in kedalaman_yang_diuji:
    model = DecisionTreeRegressor(max_depth=kedalaman, random_state=42)

    score = cross_val_score(model, X_sepeda, y_sepeda, cv=5, scoring='neg_mean_squared_error')
    rata_rata_score = score.mean()

    print(f'Max Depth: {kedalaman}, Mean CV MSE: {-rata_rata_score:.2f}')

    if rata_rata_score > skor_terbaik:
        skor_terbaik = rata_rata_score
        kedalaman_terbaik = kedalaman

print(f'\nKedalaman Terbaik: {kedalaman_terbaik} dengan Mean CV MSE: {-skor_terbaik:.2f}')

#-------------------------------------------
# penyempurnaan otomatis dengan GridSearchCV
#-------------------------------------------
from sklearn.model_selection import GridSearchCV, train_test_split

X_Train, y_Train = make_regression(n_samples=500, n_features=3, noise=15, random_state=42)

param_grid = {
    'max_depth': [2, 3, 5, 7, 10, 15],
    'min_samples_split': [2, 5, 10]
}

grid_search = GridSearchCV(DecisionTreeRegressor(), param_grid, cv=5)
grid_search.fit(X_Train, y_Train)

print(f'Best Parameters: {grid_search.best_params_}')

#--------------------------------------------------
# penyempurnaan otomatis (dataset kanker payudara)
#--------------------------------------------------
print("--- Studi Kasus 2: Penyempurnaan Otomatis (GridSearchCV) ---")

data_kanker = load_breast_cancer()
X_kanker = data_kanker.data
y_kanker = data_kanker.target

X_train_kanker, X_test_kanker, y_train_kanker, y_test_kanker = train_test_split(X_kanker, y_kanker, test_size=0.2, random_state=42)

param_grid_kanker = {
    'max_depth': [2, 3, 5, 7, 10],
    'min_samples_split': [2, 5, 10],
    'criterion': ['gini', 'entropy']
}

print("Melakukan GridSearchCV untuk dataset kanker payudara...")
grid_search_kanker = GridSearchCV(DecisionTreeClassifier(random_state=42), param_grid_kanker, cv=5, scoring='accuracy')
grid_search_kanker.fit(X_train_kanker, y_train_kanker)

# Menampilkan hasil terbaik
print(f'Best Parameters: {grid_search_kanker.best_params_}')
print(f'Best CV Accuracy: {grid_search_kanker.best_score_:.4f}')

# Evaluasi model terbaik pada data test
best_model_kanker = grid_search_kanker.score(X_test_kanker, y_test_kanker)
print(f'Test Accuracy of Best Model: {best_model_kanker:.4f}')