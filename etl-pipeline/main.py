import extract
import transform
import load

def run_etl():
    print("Starting ETL pipeline...")

    raw_filename = extract.extract_jobs()      
    clean_filename = transform.transform_jobs(raw_filename)   
    load.load_jobs(clean_filename)             

    print("ETL pipeline finished successfully!")

if __name__ == "__main__":
    run_etl()