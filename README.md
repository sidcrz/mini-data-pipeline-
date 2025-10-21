# 🚀 Mini Data Pipeline — Python + PostgreSQL + Docker (Deployed on Google Cloud)

This project marks my first cloud-based ETL workflow, built step by step inside a Google Cloud VM using Docker, PostgreSQL, and Python (pandas + SQLAlchemy).

---

## 🧠 Architecture Diagram

Here’s how the entire mini data pipeline fits together:

```

+---------------------------+
|      Python Script        |
|  (pandas + SQLAlchemy)    |
|  Extract + Transform Data |
+------------+--------------+
             |
             v
+---------------------------+
|   PostgreSQL (Docker)     |
|   demo database container |
+------------+--------------+
             |
             v
+---------------------------+
|   Query + Verify Results  |
+---------------------------+
             |
             v
+---------------------------+
| Google Cloud VM (Ubuntu)  |
|  Environment where all    |
|  components are deployed  |
+---------------------------+

```
---

## 💬 How It All Works (In Simple Terms)

This setup is like building a small data factory.

Raw data comes in, gets cleaned and organized, and is finally stored neatly so analysts or dashboards can use it.  
Here’s how each part fits in:

- 🐳 Docker acts like a safe box that runs your database in isolation — no messy installations or version conflicts.
- 🐘 PostgreSQL is your warehouse where all the transformed data is stored.
- 🐍 Python is the worker who moves the data, cleans it, and loads it into the warehouse.
- ☁️ Google Cloud VM is your remote workspace, similar to a mini production server where everything runs together.

It’s simple, reproducible, and mirrors the foundation of how modern data pipelines work.

---

## 🧭 Why This Project Matters

Every modern company — Netflix, Uber, Spotify, Airbnb — depends on a process like this every single day.  
Their data engineers build pipelines that collect raw data, clean it, and prepare it for analytics or machine learning.

This project helped me:
- Understand the core ETL (Extract, Transform, Load) process  
- Learn how Docker keeps services consistent and portable  
- Use Python’s pandas and SQLAlchemy to automate data flows  
- Simulate a small production-like environment on Google Cloud  

Even though this project is small, it captures the real mindset of a Data Engineer — building reliable, repeatable systems that move data efficiently.

---

## ⚡️ Under the Hood (What Really Happens)

1. A PostgreSQL container is launched using Docker and configured to persist data inside a local volume.  
2. A Python ETL script extracts mock data, performs transformations with pandas, and loads it into PostgreSQL using SQLAlchemy.  
3. Everything runs seamlessly inside a Google Cloud VM — imitating a true production setup.  
4. I connect directly to the PostgreSQL database to verify that the transformed data is successfully loaded.

This workflow covers the exact building blocks that scale later into complex, automated data systems.

---

## 🌍 Real-World Analogy

Think of this setup like cooking a meal:

Component | Real-World Role
-----------|----------------
🐍 Python | The chef who prepares and cleans the ingredients (raw data)
🐘 PostgreSQL | The kitchen counter where the finished dishes (clean data) are served
🐳 Docker | The kitchen setup that can be moved anywhere without breaking anything
☁️ Google Cloud VM | The restaurant space where your kitchen runs and customers (analysts, dashboards) are served

Once you understand this small pipeline, you can scale it up easily — adding Airflow for scheduling, dbt for transformations, or Spark for big data processing.


## 🧩 2. Run PostgreSQL in a Docker Container

With the environment ready, I set up PostgreSQL inside Docker.  
This keeps everything portable and avoids local installation issues.

```
docker run -d \
  --name postgres \
  -e POSTGRES_PASSWORD=admin \
  -e POSTGRES_DB=demo \
  -p 5432:5432 \
  -v pgdata:/var/lib/postgresql/data \
  postgres 
  ```

Explanation:
```
- -d runs the container in the background  
- --name postgres gives it a friendly name  
- -e POSTGRES_PASSWORD and -e POSTGRES_DB set environment variables  
- -p 5432:5432 exposes the database to the host  
- -v pgdata ensures persistent storage

```

Verify it’s running:

docker ps

Expected:
CONTAINER ID   IMAGE      STATUS          PORTS                    NAMES
xxxxxx         postgres   Up ...          0.0.0.0:5432->5432/tcp   postgres

---

## 🧩 3. Set Up the Python Environment

Next, I created a Python virtual environment for this project.  
It’s good practice to keep dependencies isolated and organized.

sudo apt install python3-venv -y
python3 -m venv venv
source venv/bin/activate

Install dependencies:
pip install pandas sqlalchemy psycopg2-binary

Library | Role
---------|-----
pandas | Data cleaning and transformation
SQLAlchemy | Database connection and ORM
psycopg2-binary | PostgreSQL driver

---

## 🧩 4. Build the ETL Script

Here’s the full ETL script that extracts mock data, transforms it, and loads it into PostgreSQL.

etl_script.py

```
import pandas as pd
from sqlalchemy import create_engine 
```

# Step 1: Extract
```
data = {
    'id': [1, 2, 3],
    'name': ['Alice', 'Bob', 'Clara'],
    'country': ['USA', 'India', 'UK']
}
df = pd.DataFrame(data)
print("✅ Data extracted successfully")
```

# Step 2: Transform
```
df['name'] = df['name'].str.upper()
print("🔄 Data transformed successfully")
```

# Step 3: Load
```
engine = create_engine('postgresql://postgres:admin@localhost:5432/demo')
df.to_sql('customers', engine, if_exists='replace', index=False)
print("📦 Data loaded into PostgreSQL successfully!")
```

Run it:
```
python3 etl_script.py
```

Expected output:
✅ Data extracted successfully
🔄 Data transformed successfully
📦 Data loaded into PostgreSQL successfully!

---

## 🧩 5. Verify the Data in PostgreSQL

Finally, I connected to PostgreSQL to make sure the ETL worked.

```
docker exec -it postgres psql -U postgres -d demo
```

Inside the psql prompt:

SELECT * FROM customers;
```
Output:
 id |  name  | country
----+--------+---------
  1 | ALICE  | USA
  2 | BOB    | India
  3 | CLARA  | UK
(3 rows)
```
✅ The ETL worked perfectly — data extracted, cleaned, and stored successfully.

---

## 🧩 6. Organize the Project
```
mini-data-pipeline/
│
├── etl_script.py
├── requirements.txt
├── .gitignore
├── Dockerfile (optional)
├── README.md
└── screenshots/
    ├── 01_vm_created.png
    ├── 02_vm_ssh.png
    ├── 03_docker_ready.png
    ├── 04_postgres_pull.png
    ├── 05_postgres_running.png
    ├── 06_venv_active.png
    ├── 07_pip_installed.png
    ├── 08_etl_success.png
    └── 09_sql_output.png

```
This organization keeps the project clean, reproducible, and ready for version control.

---

## 🎓 What I Learned

- How to use Docker for persistent, portable databases  
- How to connect Python → PostgreSQL using SQLAlchemy  
- The full ETL lifecycle (extract, transform, load)  
- How to run pipelines in a cloud-based environment  

These are the exact building blocks for every modern data stack.

---

