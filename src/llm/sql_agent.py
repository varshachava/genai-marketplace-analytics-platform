import openai

class SQLAgent:

    def __init__(self, api_key):

        openai.api_key = api_key

    def generate_sql(self, question):

        prompt = f"""
You are an analytics assistant for an AI data marketplace.

Convert the following analytics question into SQL.

Table:
marketplace_tasks(task_id, region, task_type,
worker_id, completion_time, task_cost, quality_score)

Question:
{question}

Return SQL query only.
"""

        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role":"user","content":prompt}]
        )

        return response["choices"][0]["message"]["content"]
