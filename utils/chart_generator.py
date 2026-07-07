import plotly.express as px


def generate_chart(df):

    if df.empty:
        return None

    if len(df.columns) < 2:
        return None

    x = df.columns[0]
    y = df.columns[1]

    try:

        # Line chart for monthly trend
        if "month" in x.lower() or "date" in x.lower():
            return px.line(
                df,
                x=x,
                y=y,
                markers=True,
                title=f"{y} over {x}"
            )

        # Pie chart for payment methods
        elif "payment" in x.lower():
            return px.pie(
                df,
                names=x,
                values=y,
                title="Payment Distribution"
            )

        # Bar chart (default)
        else:
            return px.bar(
                df,
                x=x,
                y=y,
                text_auto=True,
                title=f"{y} by {x}"
            )

    except Exception:
        return None