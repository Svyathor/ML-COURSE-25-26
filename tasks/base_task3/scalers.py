import numpy as np
import typing


class MinMaxScaler:
    def fit(self, data: np.ndarray) -> None:
        self.data_min = np.min(data, axis=0)
        self.data_max = np.max(data, axis=0)

    def transform(self, data: np.ndarray) -> np.ndarray:
        scaled = (data - self.data_min) / (self.data_max - self.data_min)
        return scaled


class StandardScaler:
    def fit(self, data: np.ndarray) -> None:
        self.mean = np.mean(data, axis=0)
        self.std = np.std(data, axis=0)

    def transform(self, data: np.ndarray) -> np.ndarray:
        result = (data - self.mean) / self.std
        return result
