from ai.llm import ask_gemini


def generate_insights(question, dataframe):
    """
    Generate business insights from the SQL query results.
    """

    prompt = f"""
You are a senior business analyst.

A user asked:

{question}

The SQL query returned this data:

{dataframe.to_string(index=False)}

Write:

1. Three important business insights.
2. One recommendation.

Keep the answer under 150 words.
"""

    return ask_gemini(prompt)