import requests 
import pandas as pd 
import numpy as np
import datetime 

# lets create log function to record all running 
def log_key(msag):
    with open('log.txt','a') as f:
        f.write(f"the masg succesfuily write in {datetime.datetime.now()}-{msag}")
        
        
# lets rad data form url link
response=requests.get('https://jsonplaceholder.typicode.com/posts')
data=response.json()


try :
    # lets create data frame from json data
    df=pd.DataFrame(data)
    # lets print data frame
    df.to_csv('key.csv',index=False)
    
except Exception as e:
    log_key(f"error {e}")
    print(f"error {e}")
    