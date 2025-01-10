import requests
import pandas as pd 
import datetime

logfile='log_file.txt'
def log_msg(masg):
     with open(logfile, 'a') as f:
        f.write(f'{datetime.datetime.now()} - {masg} \n')
    
#lets read csv file form api
try: 
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    data = response.json()

    # Convert to DataFrame
    df = pd.DataFrame(data)

    # Transform
    df['title_length'] = df['title'].apply(len)
    df['body_length'] = df['body'].apply(len)
    etl_timestamp = datetime.datetime.now()
    df['etl_timestamp'] = etl_timestamp
#lets save tocsv 
     # Load
    df.to_csv('key1.csv', index=False)
    log_msg(f'ETL job completed at {etl_timestamp} and data saved to transformed_data.csv')

except Exception as e:
     log_msg(f"Error {e} at {datetime.datetime.now()}")
    
