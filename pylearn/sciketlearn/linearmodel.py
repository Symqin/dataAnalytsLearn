# Model linear

from sklearn.linear_model import LinearRegression, Ridge, LogisticRegression
from sklearn.datasets import make_regression, make_classification
import numpy as np
import matplotlib.pyplot as plt


# Ensure training data exists; if not, create a synthetic regression dataset
X_train, y_train = make_regression(n_samples=100, n_features=1, noise=10, random_state=0)

#---------------------------------------------
# intuisi model linear
#---------------------------------------------
# sesuaikan dengan model regresi linear model = LinearRegression()
model = LinearRegression()

model.fit(X_train, y_train)
print("Coefficients:", model.coef_)
print("Intercept:", model.intercept_)

#---------------------------------------------
# Regresi Linear 
#---------------------------------------------
y_pred = model.predict(X_train)
mse = np.mean((y_train - y_pred) ** 2)
r2 = model.score(X_train, y_train)
print(f'Mean Squared Error: {mse:.2f}')

#----------------------------------------------
# visualisasi hasil regresi linear
#----------------------------------------------
ridge = Ridge(alpha=1.0)
ridge.fit(X_train, y_train)
print(f'Ridge Coefficients: {ridge.coef_}')

#---------------------------------------------
# Regresi Logistik (model klasifikasi)
#---------------------------------------------
# Cukup ubah n_features menjadi 5
X_train_clf, y_train_clf = make_classification(n_samples=100, n_features=5, random_state=0)

# --- Regresi Logistik (Model Klasifikasi) ---
print("--- Logistic Regression ---")
log_reg = LogisticRegression()
log_reg.fit(X_train_clf, y_train_clf) # Sekarang menggunakan data klasifikasi!
print(f"Accuracy: {log_reg.score(X_train_clf, y_train_clf) * 100:.0f}%")

