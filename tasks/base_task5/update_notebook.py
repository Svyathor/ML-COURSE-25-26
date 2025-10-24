import json

with open(r'C:\Users\MindstormS\Documents\GitHub\ML-COURSE-25-26\tasks\base_task5\Linear_Models_regression.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

nb['cells'][21]['source'] = [
    "<font color='MediumOrchid'>**Ваши выводы тут:**</font>\n",
    "\n",
    "При увеличении константы регуляризации параметры модели уменьшаются по абсолютной величине. Это происходит потому что регуляризация штрафует большие значения весов. Для Ridge регрессии веса плавно уменьшаются и стремятся к нулю, но никогда его не достигают. В Lasso регрессии некоторые веса могут становиться строго равными нулю, что фактически убирает признаки из модели.\n",
    "\n",
    "Что касается качества модели - здесь нужен баланс. Если регуляризация слишком слабая (малая константа), модель может переобучиться на обучающей выборке и плохо работать на новых данных. Если регуляризация слишком сильная (большая константа), модель становится слишком простой и недообучается, не улавливая важные закономерности. Оптимальное значение константы регуляризации обычно находится где-то посередине и подбирается с помощью кросс-валидации."
]

nb['cells'][33]['source'] = [
    "np.random.seed(42)\n",
    "n_samples = 100\n",
    "\n",
    "x1_example1 = np.random.randn(n_samples)\n",
    "x2_example1 = 2 * x1_example1 + 0.001 * np.random.randn(n_samples)\n",
    "X_example1 = np.column_stack([x1_example1, x2_example1])\n",
    "y_example1 = 3 * x1_example1 + np.random.randn(n_samples) * 0.5\n",
    "\n",
    "model1 = LinearRegression()\n",
    "model1.fit(X_example1, y_example1)\n",
    "print('Пример 1 - x2 = 2*x1')\n",
    "print(f'Коэффициенты: {model1.coef_}')\n",
    "print(f'Сумма коэффициентов: {model1.coef_.sum():.4f}\\n')\n",
    "\n",
    "x1_example2 = np.random.randn(n_samples) * 2\n",
    "x2_example2 = -0.5 * x1_example2 + 0.0001 * np.random.randn(n_samples)\n",
    "X_example2 = np.column_stack([x1_example2, x2_example2])\n",
    "y_example2 = 1.5 * x1_example2 + np.random.randn(n_samples) * 0.3\n",
    "\n",
    "model2 = LinearRegression()\n",
    "model2.fit(X_example2, y_example2)\n",
    "print('Пример 2 - x2 = -0.5*x1')\n",
    "print(f'Коэффициенты: {model2.coef_}')\n",
    "print(f'Сумма коэффициентов: {model2.coef_.sum():.4f}\\n')\n",
    "\n",
    "x1_example3 = np.linspace(-3, 3, n_samples)\n",
    "x2_example3 = 5 * x1_example3\n",
    "X_example3 = np.column_stack([x1_example3, x2_example3])\n",
    "y_example3 = 2 * x1_example3 + np.random.randn(n_samples) * 0.2\n",
    "\n",
    "model3 = LinearRegression()\n",
    "model3.fit(X_example3, y_example3)\n",
    "print('Пример 3 - x2 = 5*x1 (точная зависимость)')\n",
    "print(f'Коэффициенты: {model3.coef_}')\n",
    "print(f'Определитель X.T @ X: {np.linalg.det(X_example3.T @ X_example3):.2e}')"
]

nb['cells'][43]['source'] = [
    "scaler = StandardScaler()\n",
    "\n",
    "X_train_scaled = scaler.fit_transform(X_train)\n",
    "X_test_scaled = scaler.transform(X_test)"
]

nb['cells'][48]['source'] = [
    "<font color='MediumOrchid'>**Ваши выводы тут:**</font>\n",
    "\n",
    "Основное преимущество RMSE перед MSE в том, что RMSE измеряется в тех же единицах, что и целевая переменная. Например, если мы предсказываем цену квартиры в рублях, то MSE будет в рублях в квадрате, а RMSE - просто в рублях. Это делает RMSE гораздо более интерпретируемой метрикой.\n",
    "\n",
    "Еще один плюс RMSE - она более чувствительна к большим ошибкам по сравнению с MAE, но при этом не так сильно как MSE. То есть RMSE находится где-то посередине по чувствительности к выбросам. Это полезно когда мы хотим штрафовать большие ошибки, но не слишком сильно."
]

nb['cells'][61]['source'] = [
    "model_lasso = Pipeline([\n",
    "    ('scaler', StandardScaler()),\n",
    "    ('regr', Lasso())\n",
    "])\n",
    "\n",
    "model_ridge = Pipeline([\n",
    "    ('scaler', StandardScaler()),\n",
    "    ('regr', Ridge())\n",
    "])\n",
    "\n",
    "lasso_cv = GridSearchCV(\n",
    "    model_lasso,\n",
    "    cv=5,\n",
    "    scoring='neg_root_mean_squared_error',\n",
    "    param_grid={'regr__alpha': np.logspace(-3, 3, 10)}\n",
    ")\n",
    "\n",
    "ridge_cv = GridSearchCV(\n",
    "    model_ridge,\n",
    "    cv=5,\n",
    "    scoring='neg_root_mean_squared_error',\n",
    "    param_grid={'regr__alpha': np.logspace(-3, 3, 10)}\n",
    ")\n",
    "\n",
    "lasso_cv.fit(X_train, y_train)\n",
    "ridge_cv.fit(X_train, y_train)\n",
    "\n",
    "y_pred_lasso = lasso_cv.predict(X_test)\n",
    "y_pred_ridge = ridge_cv.predict(X_test)\n",
    "\n",
    "rmse_lasso = mean_squared_error(y_test, y_pred_lasso, squared=False)\n",
    "rmse_ridge = mean_squared_error(y_test, y_pred_ridge, squared=False)\n",
    "\n",
    "print(f'Lasso RMSE: {rmse_lasso:.4f}')\n",
    "print(f'Lasso лучший alpha: {lasso_cv.best_params_[\"regr__alpha\"]:.4f}')\n",
    "print(f'\\nRidge RMSE: {rmse_ridge:.4f}')\n",
    "print(f'Ridge лучший alpha: {ridge_cv.best_params_[\"regr__alpha\"]:.4f}')"
]

with open(r'C:\Users\MindstormS\Documents\GitHub\ML-COURSE-25-26\tasks\base_task5\Linear_Models_regression.ipynb', 'w', encoding='utf-8') as f:
    json.dump(nb, f, ensure_ascii=False, indent=1)

print('Notebook updated successfully!')
