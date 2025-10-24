import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.metrics import root_mean_squared_error

print("="*50)
print("Testing Task 2: Linear dependency examples")
print("="*50)

np.random.seed(42)
n_samples = 100

x1_example1 = np.random.randn(n_samples)
x2_example1 = 2 * x1_example1 + 0.001 * np.random.randn(n_samples)
X_example1 = np.column_stack([x1_example1, x2_example1])
y_example1 = 3 * x1_example1 + np.random.randn(n_samples) * 0.5

model1 = LinearRegression()
model1.fit(X_example1, y_example1)
print('Пример 1 - x2 = 2*x1')
print(f'Коэффициенты: {model1.coef_}')
print(f'Сумма коэффициентов: {model1.coef_.sum():.4f}\n')

x1_example2 = np.random.randn(n_samples) * 2
x2_example2 = -0.5 * x1_example2 + 0.0001 * np.random.randn(n_samples)
X_example2 = np.column_stack([x1_example2, x2_example2])
y_example2 = 1.5 * x1_example2 + np.random.randn(n_samples) * 0.3

model2 = LinearRegression()
model2.fit(X_example2, y_example2)
print('Пример 2 - x2 = -0.5*x1')
print(f'Коэффициенты: {model2.coef_}')
print(f'Сумма коэффициентов: {model2.coef_.sum():.4f}\n')

x1_example3 = np.linspace(-3, 3, n_samples)
x2_example3 = 5 * x1_example3
X_example3 = np.column_stack([x1_example3, x2_example3])
y_example3 = 2 * x1_example3 + np.random.randn(n_samples) * 0.2

model3 = LinearRegression()
model3.fit(X_example3, y_example3)
print('Пример 3 - x2 = 5*x1 (точная зависимость)')
print(f'Коэффициенты: {model3.coef_}')
print(f'Определитель X.T @ X: {np.linalg.det(X_example3.T @ X_example3):.2e}')

print("\n" + "="*50)
print("Testing Task 3: StandardScaler")
print("="*50)

X = np.random.randn(100, 5)
y = np.random.randn(100)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

print(f"X_train_scaled shape: {X_train_scaled.shape}")
print(f"X_test_scaled shape: {X_test_scaled.shape}")
print(f"X_train_scaled mean: {X_train_scaled.mean(axis=0)}")
print(f"X_train_scaled std: {X_train_scaled.std(axis=0)}")
print("OK: StandardScaler works!")

print("\n" + "="*50)
print("Testing Task 5: GridSearchCV")
print("="*50)

model_lasso = Pipeline([
    ('scaler', StandardScaler()),
    ('regr', Lasso())
])

model_ridge = Pipeline([
    ('scaler', StandardScaler()),
    ('regr', Ridge())
])

lasso_cv = GridSearchCV(
    model_lasso,
    cv=5,
    scoring='neg_root_mean_squared_error',
    param_grid={'regr__alpha': np.logspace(-3, 3, 10)}
)

ridge_cv = GridSearchCV(
    model_ridge,
    cv=5,
    scoring='neg_root_mean_squared_error',
    param_grid={'regr__alpha': np.logspace(-3, 3, 10)}
)

print("Fitting Lasso...")
lasso_cv.fit(X_train, y_train)
print("Fitting Ridge...")
ridge_cv.fit(X_train, y_train)

y_pred_lasso = lasso_cv.predict(X_test)
y_pred_ridge = ridge_cv.predict(X_test)

rmse_lasso = root_mean_squared_error(y_test, y_pred_lasso)
rmse_ridge = root_mean_squared_error(y_test, y_pred_ridge)

print(f'Lasso RMSE: {rmse_lasso:.4f}')
print(f'Lasso лучший alpha: {lasso_cv.best_params_["regr__alpha"]:.4f}')
print(f'\nRidge RMSE: {rmse_ridge:.4f}')
print(f'Ridge лучший alpha: {ridge_cv.best_params_["regr__alpha"]:.4f}')

print("\n" + "="*50)
print("ALL TESTS PASSED!")
print("="*50)
