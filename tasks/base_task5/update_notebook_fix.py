import json

with open(r'C:\Users\MindstormS\Documents\GitHub\ML-COURSE-25-26\tasks\base_task5\Linear_Models_regression.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

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
    "from sklearn.metrics import root_mean_squared_error\n",
    "rmse_lasso = root_mean_squared_error(y_test, y_pred_lasso)\n",
    "rmse_ridge = root_mean_squared_error(y_test, y_pred_ridge)\n",
    "\n",
    "print(f'Lasso RMSE: {rmse_lasso:.4f}')\n",
    "print(f'Lasso лучший alpha: {lasso_cv.best_params_[\"regr__alpha\"]:.4f}')\n",
    "print(f'\\nRidge RMSE: {rmse_ridge:.4f}')\n",
    "print(f'Ridge лучший alpha: {ridge_cv.best_params_[\"regr__alpha\"]:.4f}')"
]

with open(r'C:\Users\MindstormS\Documents\GitHub\ML-COURSE-25-26\tasks\base_task5\Linear_Models_regression.ipynb', 'w', encoding='utf-8') as f:
    json.dump(nb, f, ensure_ascii=False, indent=1)

print('Notebook fixed!')
