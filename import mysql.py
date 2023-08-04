import mysql.connector
import pandas as pd
import os
import tkinter as tk
from tkinter import filedialog


# Replace the following placeholders with your actual MySQL database credentials
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "s0lutus#21",
    "database": "PS_DB",
}

try:
    # Connect to the MySQL server
    connection = mysql.connector.connect(**db_config)

    if connection.is_connected():
        print("Connected to MySQL database.")

        # Perform database operations here (e.g., execute queries, fetch data, etc.)


except mysql.connector.Error as e:
    print(f"Error while connecting to MySQL: {e}")


file_path = filedialog.askopenfilename()

df = pd.read_csv(file_path)

df = df.where(pd.notna(df), None)



df.to_sql(name=table_name, con=db_connection, if_exists="replace", index=False)