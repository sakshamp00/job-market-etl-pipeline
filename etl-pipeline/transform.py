import json
import os
import pandas as pd
from glob import glob

def transform_jobs(raw_file):
    os.makedirs('cleanData', exist_ok=True)
    print("Transforming job data...")
    timestamp = raw_file.split("_")[-2] + "_" + raw_file.split("_")[-1].replace(".json", "")

    with open(raw_file) as json_data:
        parsed_data = json.load(json_data)
        jobsList = parsed_data["data"]
        
    fields = ["job_title", "employer_name", "job_city", "job_state", "job_country", "job_posted_at_datetime_utc", "job_apply_link", "job_description"]
    clean_data_list = []
    for job in jobsList:
        job_record = {}
        for field in fields:
            job_record[field] = job.get(field, "")
        job_record["extracted_at"] = timestamp  
        clean_data_list.append(job_record) 
    clean_filename = f"cleanData/jobs_clean_{timestamp}.csv"
    df = pd.DataFrame(clean_data_list)
    df = df.drop_duplicates(subset=["job_title", "employer_name", "job_city"])
    df.to_csv(clean_filename, index=False)
    print(f"Saved clean data → {clean_filename}")
    return clean_filename