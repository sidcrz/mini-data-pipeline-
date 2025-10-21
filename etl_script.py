"""
Mini Data Pipeline
------------------
Author: Siddhartha Chauhan

This script simulates a simple ETL process:
1. Extract sample data
2. Transform it using pandas
3. Load it into a PostgreSQL database running in Docker
"""

import pandas as pd
from sqlalchemy import create_engine

# Step 1: Extract
data = {
    'id': [1, 2, 3],
    'name': ['Alice', 'Bob', 'Clara'],
    'country': ['USA', 'India', 'UK']
}
df = pd.DataFrame(data)
print("✅ Data extracted successfully")

# Step 2: Transform
df['name'] = df['name'].str.upper()
print("🔄 Data transformed successfully")

# Step 3: Load
# Database connection string -> postgresql://<user>:<password>@<host>:<port>/<db_name>
engine = create_engine('postgresql://postgres:admin@localhost:5432/demo')

df.to_sql('customers', engine, if_exists='replace', index=False)
print("📦 Data loaded into PostgreSQL successfully!")
