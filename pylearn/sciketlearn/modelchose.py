import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from sklearn.datasets import make_regression
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.linear_model import LinearRegression

#--------------------------------------------
# Overfitting dan Underfitting
#--------------------------------------------

# Membuat dataset regresi
x, y = make_regression(n_samples=100, n_features=1, noise=20, random_state=42)
# Membagi dataset menjadi training dan testing
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

from sklearn.tree import DecisionTreeRegressor 
train_score = []
test_score = []

for depth in range(1, 10):
    model = DecisionTreeRegressor(max_depth=depth)
    model.fit(x_train, y_train)
    train_score.append(model.score(x_train, y_train))
    test_score.append(model.score(x_test, y_test))

plt.plot(range(1, 10), train_score, label='Train Score')
plt.plot(range(1, 10), test_score, label='Test Score')
plt.legend()
plt.show()

#---------------------------------------------
# kurva validasi dan kurva belajar
#---------------------------------------------
from sklearn.model_selection import learning_curve

train_sizes, train_scores, test_scores = learning_curve(
    LinearRegression(), x, y, cv=5, scoring='neg_mean_squared_error')

train_mean = -train_scores.mean(axis=1)
test_mean = -test_scores.mean(axis=1)
plt.plot(train_sizes, train_mean, label='Train MSE')
plt.plot(train_sizes, test_mean, label='Test MSE')
plt.legend()
plt.show()

#---------------------------------------------
# Trade off Bias dan Variance
#---------------------------------------------

from sklearn.linear_model import Ridge
from sklearn.model_selection import cross_val_score

# membandingkan linar regression dengan ridge regression
linar_model = cross_val_score(LinearRegression(), x, y, cv=5, scoring='neg_mean_squared_error').mean()
ridge_model = cross_val_score(Ridge(alpha=1.0), x, y, cv=5, scoring='neg_mean_squared_error').mean()
print(f'Linear Regression MSE: {-linar_model}')
print(f'Ridge Regression MSE: {-ridge_model}')
