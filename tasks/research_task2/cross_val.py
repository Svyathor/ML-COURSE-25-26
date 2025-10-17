import numpy as np
import typing
from collections import defaultdict


def kfold_split(num_objects: int,
                num_folds: int) -> list[tuple[np.ndarray, np.ndarray]]:
    """Split [0, 1, ..., num_objects - 1] into equal num_folds folds
       (last fold can be longer) and returns num_folds train-val
       pairs of indexes.

    Parameters:
    num_objects: number of objects in train set
    num_folds: number of folds for cross-validation split

    Returns:
    list of length num_folds, where i-th element of list
    contains tuple of 2 numpy arrays, he 1st numpy array
    contains all indexes without i-th fold while the 2nd
    one contains i-th fold
    """
    indices = np.arange(num_objects)
    fold_size = num_objects // num_folds
    result = []

    for i in range(num_folds):
        start = i * fold_size
        if i == num_folds - 1:
            end = num_objects
        else:
            end = (i + 1) * fold_size

        val_indices = indices[start:end]
        train_indices = np.concatenate([indices[:start], indices[end:]])
        result.append((train_indices, val_indices))

    return result


def knn_cv_score(X: np.ndarray, y: np.ndarray, parameters: dict[str, list],
                 score_function: callable,
                 folds: list[tuple[np.ndarray, np.ndarray]],
                 knn_class: object) -> dict[str, float]:
    """Takes train data, counts cross-validation score over
    grid of parameters (all possible parameters combinations)

    Parameters:
    X: train set
    y: train labels
    parameters: dict with keys from
        {n_neighbors, metrics, weights, normalizers}, values of type list,
        parameters['normalizers'] contains tuples (normalizer, normalizer_name)
        see parameters example in your jupyter notebook

    score_function: function with input (y_true, y_predict)
        which outputs score metric
    folds: output of kfold_split
    knn_class: class of knn model to fit

    Returns:
    dict: key - tuple of (normalizer_name, n_neighbors, metric, weight),
    value - mean score over all folds
    """
    results = defaultdict(list)

    for normalizer, normalizer_name in parameters['normalizers']:
        for n_neighbors in parameters['n_neighbors']:
            for metric in parameters['metrics']:
                for weight in parameters['weights']:
                    for train_idx, val_idx in folds:
                        X_train_fold = X[train_idx]
                        y_train_fold = y[train_idx]
                        X_val_fold = X[val_idx]
                        y_val_fold = y[val_idx]

                        if normalizer is not None:
                            normalizer_fitted = type(normalizer)()
                            normalizer_fitted.fit(X_train_fold)
                            X_train_fold = normalizer_fitted.transform(X_train_fold)
                            X_val_fold = normalizer_fitted.transform(X_val_fold)

                        knn = knn_class(
                            n_neighbors=n_neighbors,
                            metric=metric,
                            weights=weight
                        )
                        knn.fit(X_train_fold, y_train_fold)
                        y_pred = knn.predict(X_val_fold)
                        score = score_function(y_val_fold, y_pred)
                        key = (normalizer_name, n_neighbors, metric, weight)
                        results[key].append(score)

    mean_results = {}
    for key, scores in results.items():
        mean_results[key] = np.mean(scores)

    return mean_results
