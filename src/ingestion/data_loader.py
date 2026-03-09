import pandas as pd

class DataLoader:

    def __init__(self, path):
        self.path = path

    def load_dataset(self):

        df = pd.read_csv(self.path)

        df["completion_time"] = df["completion_time"].astype(float)
        df["task_cost"] = df["task_cost"].astype(float)
        df["quality_score"] = df["quality_score"].astype(float)

        return df

    def clean_data(self, df):

        df = df.drop_duplicates()

        df = df[df["completion_time"] > 0]

        return df
