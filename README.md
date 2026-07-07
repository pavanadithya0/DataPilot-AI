# 📊 DataPilot AI

> **AI-Powered Business Intelligence Dashboard**
>
> Convert natural language into SQL queries, analyze business data, and visualize insights using AI.

---

## 🚀 Overview

DataPilot AI is an interactive Business Intelligence dashboard built with **Python**, **Streamlit**, **SQLite**, **Plotly**, and **Google Gemini AI**.

Users can ask business questions in plain English, and the application automatically generates SQL queries, executes them on a SQLite database, visualizes the results, and provides AI-generated business insights.

---

## ✨ Features

- 🤖 Natural Language to SQL
- 📊 Interactive Dashboard
- 📈 KPI Cards
- 📉 Automatic Data Visualization
- 🗄 SQLite Database Integration
- 📥 CSV Export
- 📚 Database Explorer
- 🕒 Query History
- 💡 AI Business Insights
- ⚡ Local SQL Templates (works even when AI quota is exhausted)

---

## 📷 Screenshots

### Dashboard

https://drive.google.com/drive/folders/1tARwtNH2k9insxt9rpH-xynG93XSL_je?usp=sharing


## 🛠 Tech Stack

### Frontend

- Streamlit

### Backend

- Python

### Database

- SQLite
- SQLAlchemy

### Data Analysis

- Pandas

### Visualization

- Plotly

### AI

- Google Gemini API

---

## 📂 Project Structure

```
DataPilot-AI/
│
├── ai/
│   ├── llm.py
│   ├── sql_executor.py
│   ├── sql_generator.py
│   └── insights.py
│
├── database/
│   └── business.db
│
├── pages/
│   └── 1_Database_Explorer.py
│
├── streamlit_app/
│   └── app.py
│
├── utils/
│   ├── chart_generator.py
│   └── kpi.py
│
├── screenshots/
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙ Installation

### Clone the repository

```bash
git clone https://github.com/pavanadithya0/DataPilot-AI.git
```

---

### Navigate to the project

```bash
cd DataPilot-AI
```

---

### Create a virtual environment

```bash
python -m venv venv
```

---

### Activate the virtual environment

#### Windows

```bash
venv\Scripts\activate
```

#### macOS/Linux

```bash
source venv/bin/activate
```

---

### Install dependencies

```bash
pip install -r requirements.txt
```

---

### Configure Environment Variables

Create a `.env` file in the project root:

```env
GOOGLE_API_KEY=YOUR_GEMINI_API_KEY
```

---

### Run the application

```bash
streamlit run streamlit_app/app.py
```

---

## 💬 Example Questions

Try asking:

- Show top 10 customers by revenue
- Monthly revenue
- Revenue by state
- Orders by region
- Payment method distribution
- Top selling products
- Inventory below reorder level

---

## 📊 KPIs

The dashboard displays:

- Total Customers
- Total Orders
- Total Revenue
- Average Order Value

---

## 🔮 Future Improvements

- Authentication
- Multiple database support
- Cloud database integration
- Advanced AI insights
- Forecasting & predictive analytics
- Export to Excel and PDF
- Interactive dashboard filters
- Dark mode

---

## 👨‍💻 Author

**Pavan Adithya**

GitHub:
https://github.com/YOUR_USERNAME

LinkedIn:
https://www.linkedin.com/in/YOUR_LINKEDIN/

---

## 📄 License

This project is licensed under the MIT License.

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.
