import extract
import transform
import load

def run_etl():
    print("Starting ETL pipeline...")

    extract.extract_jobs()      
    transform.transform_jobs()   
    load.load_jobs()             

    print("ETL pipeline finished successfully!")
