# model decision tree
from sklearn.datasets import make_regression, make_classification
from sklearn.tree import DecisionTreeRegressor, DecisionTreeClassifier, export_text
from sklearn.model_selection import GridSearchCV

X_train , y_train = make_regression(n_samples=100, n_features=1, noise=10, random_state=0)
x_test, y_test = make_classification(n_samples=100, n_features=5, random_state=0)

# intuisi model decision tree
tree = DecisionTreeRegressor(max_depth=3)
tree.fit(X_train, y_train)

rules = export_text(tree, feature_names=['Feature 1'])
print(rules)

# decision tree untuk klasifikasi
tree_clf = DecisionTreeClassifier(max_depth=3)
tree_clf.fit(x_test, y_test)
accuracy = tree_clf.score(x_test, y_test)
print(f'Accuracy: {accuracy:.2f}')

#decision tree untuk regresi
tree_reg = DecisionTreeRegressor(max_depth=3)
tree_reg.fit(X_train, y_train)

# hiperparameter tuning dengan GridSearchCV
param_grid = {'max_depth': [3, 5, 10]}
grid_search = GridSearchCV(DecisionTreeRegressor(), param_grid, cv=5)
grid_search.fit(X_train, y_train)


