# 🚀 Mini ETL Pipeline (CSV → BigQuery)

## 📌 Project Overview

This project demonstrates a complete end-to-end ETL (Extract, Transform, Load) pipeline built using Python and Google BigQuery. The pipeline reads structured data from a CSV file, performs data cleaning and transformation using Pandas, and loads the processed data into Google BigQuery for analytics.

---

## 🏗️ Architecture

```
CSV File → Python (Pandas ETL)
          → Data Cleaning & Transformation
          → Google BigQuery (Data Warehouse)
```

---

## ⚙️ Tech Stack

* **Python** – Core ETL scripting language
* **Pandas** – Data manipulation and cleaning
* **Google Cloud BigQuery** – Cloud data warehouse
* **Google Cloud Service Account** – Authentication for secure access
* **PyArrow** – DataFrame to BigQuery conversion

---

## 📂 Project Structure

```
mini-etl-pipeline/
│── extract.py
│── transform.py
│── load.py
│── sales_data.csv
│── .gitignore
│── README.md
```

---

## 🔄 ETL Workflow

### 1️⃣ Extract

* Reads data from `sales_data.csv` using Pandas

### 2️⃣ Transform

* Handles missing values:

  * `amount` → filled with 0
  * `city` → filled with "Unknown"
* Ensures clean structured dataset

### 3️⃣ Load

* Uses Google BigQuery Python client
* Loads transformed data into BigQuery table:

  ```
  mini-etl-project-493720.etl_dataset.sales_table
  ```

---

## 🔐 Authentication

This project uses a **Google Cloud Service Account JSON key** for authentication.

* Secure access to BigQuery
* Avoids manual login
* Enables programmatic data loading

---

## 🚀 How to Run

### 1. Install dependencies

```bash
pip install pandas google-cloud-bigquery pyarrow
```

### 2. Set up credentials

```bash
set GOOGLE_APPLICATION_CREDENTIALS=path/to/service-account.json
```

### 3. Run pipeline

```bash
python load.py
```

---

## 📊 Output

Data is loaded into Google BigQuery table:

```
project: mini-etl-project-493720
dataset: etl_dataset
table: sales_table
```

---

## ⚠️ Challenges Faced & Solutions

### 1. BigQuery Authentication Error

* **Issue:** DefaultCredentialsError
* **Fix:** Used Service Account JSON and environment variable setup

### 2. Missing Dependency (pyarrow)

* **Issue:** DataFrame load failed
* **Fix:** Installed `pyarrow` package

### 3. Git Push Authentication Issues

* **Issue:** Wrong repo URL
* **Fix:** Corrected GitHub remote origin

---

## 💡 Key Learnings

* Building ETL pipelines using Python
* Working with cloud data warehouses (BigQuery)
* Service account authentication in GCP
* Data cleaning using Pandas
* Debugging real-world cloud integration issues
* Git & GitHub workflow for version control

---

## 📈 Future Improvements

* Convert into Airflow DAG pipeline
* Add logging & monitoring
* Containerize using Docker
* Automate deployment using CI/CD

---

## 👩‍💻 Author

Chandrika Karavadi

---

