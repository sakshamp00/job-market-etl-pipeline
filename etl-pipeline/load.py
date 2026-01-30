import sqlite3
import pandas as pd
from glob import glob
import os

def load_jobs(clean_file):
    os.makedirs('database', exist_ok=True)

    conn = sqlite3.connect('database/jobs.db')
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS jobs (
        job_title TEXT,
        employer_name TEXT,
        job_city TEXT,
        job_state TEXT,
        job_country TEXT,
        job_posted_at_datetime_utc TEXT,
        job_apply_link TEXT,
        job_description TEXT,
        extracted_at TEXT,
        PRIMARY KEY (job_title, employer_name, job_city))""")

    df = pd.read_csv(clean_file)
    c.executemany("""
                    INSERT OR IGNORE INTO jobs (
                        job_title, employer_name, job_city, job_state, job_country,
                        job_posted_at_datetime_utc, job_apply_link, job_description, extracted_at
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""", df.values.tolist())
    conn.commit()
    conn.close()
    print(f"Loaded data from {clean_file} into the database.")
    print(f"Rows in DB: {len(df)}")

