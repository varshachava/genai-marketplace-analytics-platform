class MarketplaceMetrics:

    def __init__(self, df):
        self.df = df

    def compute_metrics(self):

        metrics = {}

        metrics["total_tasks"] = len(self.df)

        metrics["average_completion_time"] = (
            self.df["completion_time"].mean()
        )

        metrics["average_task_cost"] = (
            self.df["task_cost"].mean()
        )

        metrics["average_quality"] = (
            self.df["quality_score"].mean()
        )

        metrics["tasks_by_region"] = (
            self.df.groupby("region")["task_id"].count()
        )

        return metrics
