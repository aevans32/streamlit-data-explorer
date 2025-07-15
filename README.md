# 📊 Streamlit Data Explorer

A lightweight, interactive dashboard for exploring CSV datasets using [Streamlit](https://streamlit.io/), [Pandas](https://pandas.pydata.org/), and [Matplotlib](https://matplotlib.org/).

## 👤 Author
- Andrés Evans
- linkedin.com/in/andresevans

---

## 🚀 Features

- 📁 Upload your own CSV file
- 👀 Preview the data (first 5 rows)
- 📊 View summary statistics (`df.describe()`)
- 🔎 Filter data by column and value
- 📈 Generate interactive line charts from filtered data

---

## 🖥️ Live App

Try the app on Streamlit Cloud:\
👉 [https://your-username-streamlit-data-explorer.streamlit.app](https://your-username-streamlit-data-explorer.streamlit.app) *(Replace with actual link after deployment)*

---

## 🛠️ How to Use

1. Click "Upload CSV" and select a file from your computer.
2. View the data preview and summary.
3. Use dropdowns to:
   - Filter by column and value
   - Choose which columns to plot on X and Y axes
4. Click **Generate Plot** to display the chart

---

## 📂 Example CSV Format

Your CSV should contain at least:

- One or more numeric columns (for plotting)
- One or more categorical or date columns (for filtering)

**Sample CSV structure:**

```csv
Date,Category,Value
2024-01-01,A,100
2024-01-02,B,120
2024-01-03,A,90
```

---

## 🧱 Tech Stack

- Python 3.8+
- Streamlit
- Pandas
- Matplotlib

---

## 📦 Installation (Local)

```bash
# Clone the repository
git clone https://github.com/your-username/streamlit-data-explorer.git
cd streamlit-data-explorer

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

---

## 📜 License

MIT License — feel free to use, modify, and share.

---

## 🙌 Acknowledgements

Built with ❤️ using Streamlit, for quick data exploration and visualization.

