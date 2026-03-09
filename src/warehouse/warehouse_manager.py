import pandas as pd
from sqlalchemy import create_engine

class WarehouseManager:

    def __init__(self):

        self.engine = create_engine("sqlite:///marketplace.db")

    def create_tables(self, df):

        df.to_sql(
            "marketplace_tasks",
            self.engine,
            if_exists="replace",
            index=False
        )

    def run_query(self, sql):

        result = pd.read_sql(sql, self.engine)

        return result

    def get_region_summary(self):

        query = """
        SELECT region,
        COUNT(task_id) as total_tasks,
        AVG(completion_time) as avg_time,
        AVG(task_cost) as avg_cost
        FROM marketplace_tasks
        GROUP BY region
        """

        return self.run_query(query)
