import numpy as np

class AnomalyDetector:

    def __init__(self, df):
        self.df = df

    def detect_outliers(self):

        mean_time = self.df["completion_time"].mean()

        std_time = self.df["completion_time"].std()

        threshold = mean_time + 2 * std_time

        anomalies = self.df[
            self.df["completion_time"] > threshold
        ]

        return anomalies
