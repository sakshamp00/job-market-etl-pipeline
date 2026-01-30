
# Job Market ETL Pipeline

An end-to-end Python ETL (Extract, Transform, Load) pipeline that collects job market data from a public API, cleans and deduplicates the data, and loads it into a local SQLite database for analysis.

It includes:
- Extraction of job listings from an external API (RapidAPI)
- Data cleaning, deduplication, and timestamping using Pandas
- Loading into a relational SQLite database with primary key constraints
- Modular pipeline orchestration for easy re-runs and updates

This project demonstrates core data engineering concepts such as API ingestion, data transformation with Pandas, idempotent database loading, and pipeline orchestration.

---

# 📒 Table of Contents

- [Installation](#-installation)
- [Usage](#️-usage)
- [Project Structure](#-project-structure)
- [Example Output](#-example-output)
- [Requirements](#-requirements)
- [Contributing](#-contributing)

---

# 📦 Installation

1. Clone the repo:

   ```bash
   git clone <repo-url>
   cd etl-pipeline
   ```

2. (Optional) Create and activate a virtual environment:

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Create a ```.env``` file with your API key:

    ```bash
    API_KEY=your_rapidpaikey_here
    ```

---

# 🛠️ Usage

Run the main ETL pipeline:

    python main.py
    

You’ll see the console output at each stage of the ETL process:
- Extraction of the raw job data via the API key
- Transformation and cleaning of the data
- Loading the clean data into the SQLite database

---

# 📁 Project Structure

```job-market-etl-pipeline/    # main package folder
├── etl-pipeline/              # Python module
│   ├── extract.py             # Extraction of data 
│   ├── transform.py           # Transformation of data
│   ├── load.py                # Loading data into SQLite datbase
│   └── main.py                # Entry point for executing the job market ETL pipeline
├── rawData/                   # auto-created at runtime
├── cleanData/                 # auto-created at runtime
├── database/                  # auto-created at runtime
├── .gitignore                 
├── .env                       # API key (keep at root, not inside module)
├── README.md                  # This file
└── requirements.txt           # list of Python dependencies
```

---

# 📊 Example Output

After running the pipeline:
```
Starting ETL pipeline...
Extracting job data...
Saved raw data → rawData/jobs_raw_20260130_121508.json
Transforming job data...
Saved clean data → cleanData/jobs_clean_20260130_121508.csv
Loaded data from cleanData/jobs_clean_20260130_121508.csv into the database.
Rows in DB: 19
ETL pipeline finished successfully!
```

Database verification with SQLite:
```sql
SELECT COUNT(*) FROM jobs;
SELECT job_title, employer_name FROM jobs LIMIT 5;
```

---

# 📜 Requirements

Dependencies are listed in ```requirements.txt```:
```
requests>=2.30.0
pandas>=2.1.0
python-dotenv>=1.0.0
urllib3<2
```

Install them with:
```bash
pip install -r requirements.txt
```

---

# 🤝 Contributing and Future Improvements

Contributions are welcome! Whether it’s improving the documentation, adding features like:

- Incremental loading of new jobs only
- Data visualization dashboards
- Keyword analysis or classification of jobs
- Scheduling automated ETL runs using n8n or Airflow
- Moving raw/clean data to cloud storage (S3, Google Drive)
- Sending notifications or reports after each run

Feel free to open issues or pull requests 🎉
