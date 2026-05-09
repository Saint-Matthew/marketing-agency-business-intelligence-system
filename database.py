import sqlite3
import pandas as pd

# Create connection
connection = sqlite3.connect("agency_data.db")

# Load datasets
clients_df = pd.read_csv("datasets/clients.csv")
campaigns_df = pd.read_csv("datasets/campaigns.csv")
revenue_df = pd.read_csv("datasets/revenue.csv")
employees_df = pd.read_csv("datasets/employees.csv")

# Store datasets into SQLite tables
clients_df.to_sql(
    "clients",
    connection,
    if_exists="replace",
    index=False
)

campaigns_df.to_sql(
    "campaigns",
    connection,
    if_exists="replace",
    index=False
)

revenue_df.to_sql(
    "revenue",
    connection,
    if_exists="replace",
    index=False
)

employees_df.to_sql(
    "employees",
    connection,
    if_exists="replace",
    index=False
)

print("Database created successfully.")

connection.close()
