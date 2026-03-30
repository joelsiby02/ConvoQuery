# ConvoQuery — Natural Language to SQL for Store Managers

ConvoQuery is a Natural Language to SQL (NL2SQL) system that allows store managers to query their business data using plain English — without writing any SQL.

Ask questions like:

> “What’s the total stock of Nike products under ₹2000?”

and get instant results directly from your database.

---

## 🚀 Problem It Solves

Most store managers don’t know SQL but still need quick access to business insights.

ConvoQuery removes that barrier by translating natural language into executable SQL queries using LLMs.

---

## ⚡ Features

* Convert natural language → SQL queries
* Query structured retail databases (brands, sizes, colors, pricing, stock)
* Generate business insights instantly
* Fast inference using Groq (Mistral)
* Simple UI built with Streamlit

---

## 🧠 Tech Stack

* **LLMs:** Google PaLM (legacy), Groq (Mistral)
* **Backend:** Python
* **Frontend:** Streamlit
* **Database:** MySQL / PostgreSQL

---

## 🔄 How It Works

1. User enters a query in plain English
2. LLM converts it into SQL
3. SQL is executed on the database
4. Results are displayed instantly

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/joelsiby02/ConvoQuery.git
cd ConvoQuery
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Setup environment variables

Create a `.env` file in the root directory:

```env
DB_USER=your_username
DB_PASSWORD=your_password
DB_HOST=your_host
DB_NAME=your_database

GOOGLE_API_KEY=your_google_api_key
GROQ_API_KEY=your_groq_api_key
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

Open in browser:

```
http://localhost:8501
```

---

## 💬 Example Queries

```
What is the price of a medium Puma black hoodie?
```

```
Show all available brands in the inventory
```

```
How many items are low in stock?
```

```
List products under ₹1000 with high demand
```

---

## 📁 Project Structure

```
ConvoQuery/
│── app.py
│── requirements.txt
│── .env
│── modules/
│   ├── llm_handler.py
│   ├── sql_generator.py
│   └── db_connector.py
```

---

## ⚠️ Limitations

* Accuracy depends on database schema clarity
* Complex queries may require prompt tuning
* LLM-generated SQL may occasionally be invalid

---

## 🔮 Future Improvements

* Schema-aware prompting
* Query validation and correction
* Analytics dashboard
* Role-based access control

---

## 🤝 Contributing

Pull requests are welcome. Focus areas:

* Performance
* Accuracy
* UI/UX improvements

---

## 📄 License

MIT License — see `LICENSE` file.

---

## 📝 Note

Originally built as a mini project, but designed with scalability in mind for real-world analytics use cases.
