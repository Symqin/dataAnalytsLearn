# ensemble model 
"""
Ensemble Learning adalah teknik machine learning yang 
menggabungkan beberapa model untuk menghasilkan performa 
yang lebih baik dibandingkan menggunakan satu model saja.
"""

from sklearn.datasets import make_regression, make_classification
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor, RandomForestClassifier
from sklearn.metrics import accuracy_score, mean_squared_error, f1_score
import numpy as np

X_train, y_train = make_regression(n_samples=100, n_features=1, noise=10, random_state=0)

# metode bootsrapping
rf = RandomForestRegressor(n_estimators=100)
rf.fit(X_train, y_train)

# boosting
gb = GradientBoostingRegressor(n_estimators=100)
gb.fit(X_train, y_train)

# Hyperparameter ensembling dengan GridSearchCV
param_grid = {'n_estimators': [50, 100, 200], 'max_depth': [3, 5, 10]}
grid_search_rf = GridSearchCV(RandomForestRegressor(), param_grid, cv=5)
grid_search_rf.fit(X_train, y_train)

#----------------------------------------------------------------------------
# Studi Case 1 Dataset Tipe Penutup Hutan (Klasifikasi dengan Random Forest)
#----------------------------------------------------------------------------

print("\nStudi Case 1: Dataset Tipe Penutup Hutan (Klasifikasi dengan Random Forest)")
X_hutan, y_hutan = make_classification(n_samples=1000, n_features=10, n_classes=3, n_informative=5, random_state=0)
X_train_hutan, X_test_hutan, y_train_hutan, y_test_hutan = train_test_split(X_hutan, y_hutan, test_size=0.2, random_state=0)

#model train
rf_clf = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=0)
rf_clf.fit(X_train_hutan, y_train_hutan)

#prediksi
y_pred_hutan = rf_clf.predict(X_test_hutan)
accuracy_hutan = accuracy_score(y_test_hutan, y_pred_hutan)
f1_hutan = f1_score(y_test_hutan, y_pred_hutan, average='weighted')

print(f'Accuracy: {accuracy_hutan:.2f}')
print(f'F1 Score: {f1_hutan:.2f}')

# analisis fitur
print("\nAnalisis Fitur (top 3):")
feature_importances = rf_clf.feature_importances_
top_3_features = feature_importances.argsort()[::-1][:3]
for i, feature in enumerate(top_3_features):
    print(f"{i+1}. Fitur {feature}: {feature_importances[feature]:.4f}")
print("\n")


#----------------------------------------------------------------------------
# Studi Case 2 Dataset Harga Airbnb (Regresi dengan Gradient Boosting)
#----------------------------------------------------------------------------

print("Studi Case 2: Dataset Harga Airbnb (Regresi dengan Gradient Boosting)")

X_airbnb, y_airbnb = make_regression(n_samples=1000, n_features=10, noise=20, random_state=0)
X_train_airbnb, X_test_airbnb, y_train_airbnb, y_test_airbnb = train_test_split(X_airbnb, y_airbnb, test_size=0.2, random_state=0)

#model train
gb_reg = GradientBoostingRegressor(n_estimators=150, max_depth=3, random_state=42)
gb_reg.fit(X_train_airbnb, y_train_airbnb)

#prdiksi dan evaluasi
y_pred_airbnb = gb_reg.predict(X_test_airbnb)
mse_airbnb = mean_squared_error(y_test_airbnb, y_pred_airbnb)
rmse_airbnb = np.sqrt(mse_airbnb)

print(f'Mean Squared Error: {mse_airbnb:.2f}')
print(f'Root Mean Squared Error: {rmse_airbnb:.2f}')


#----------------------------------------------------------------------------
# STUDI KASUS 3: Dataset Penjualan Online (Hyperparameter Tuning Random Forest)
#----------------------------------------------------------------------------

print("\nStudi Case 3: Dataset Penjualan Online (Hyperparameter Tuning Random Forest)")

X_penjualan, y_penjualan = make_classification(n_samples=1000, n_features=10, n_classes=2, random_state=0)
X_train_penjualan, X_test_penjualan, y_train_penjualan, y_test_penjualan = train_test_split(X_penjualan, y_penjualan, test_size=0.2, random_state=0)    

# definisikan parameter grid untuk tuning
param_grid_rf = {
    'n_estimators': [50, 100, 200],
    'max_depth': [3, 5, 10]
}

print("Melakukan Hyperparameter Tuning dengan GridSearchCV...")
grid_search = GridSearchCV(
    estimator=RandomForestClassifier(random_state=42),
    param_grid=param_grid_rf,
    cv=5,
    scoring='neg_mean_squared_error',
    n_jobs=-1
)

grid_search.fit(X_train_penjualan, y_train_penjualan)

# evaluasi model terbaik
best_rf = grid_search.best_estimator_
y_pred_penjualan = best_rf.predict(X_test_penjualan)
mse_best_rf = mean_squared_error(y_test_penjualan, y_pred_penjualan)

print(f"Best Parameters: {grid_search.best_params_}")
print(f"Best Cross-Validation Score: {-grid_search.best_score_:.2f}")
print(f"mse dengan model terbaik: {mse_best_rf:.2f}")
