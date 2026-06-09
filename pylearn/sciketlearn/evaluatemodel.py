# evaluasi kinerja model 
from sklearn.datasets import make_regression
from sklearn.dummy import DummyRegressor
from sklearn.metrics import mean_squared_error

X_train, y_train = make_regression(n_samples=100, n_features=1, noise=10, random_state=0)
X_test, y_test = make_regression(n_samples=50, n_features=1, noise=10, random_state=1)

# membandingkan model dengan baseline sederhana

dummy_reg = DummyRegressor(strategy='mean')
dummy_reg.fit(X_train, y_train)
baseline_mse = mean_squared_error(y_test, dummy_reg.predict(X_test))

# cross-validation 
from sklearn.model_selection import cross_val_score, StratifiedKFold
cv = StratifiedKFold(n_splits=5)
scores = cross_val_score(dummy_reg, X_train, y_train, cv=cv)


# nested cross-validation 
from sklearn.model_selection import KFold
outer_cv = KFold(n_splits=5)
nested_scores = cross_val_score(dummy_reg, X_train, y_train, cv=outer_cv)

# metode klasifikasi 
from sklearn.metrics import classification_report

y_pred = dummy_reg.predict(X_test)
report = classification_report(y_test, y_pred)
print("Classification Report:\n", report)

#metrik regresi
from sklearn.metrics import r2_score, mean_absolute_error

mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

