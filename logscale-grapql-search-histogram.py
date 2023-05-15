import requests
import json

url = "https://your-logscale-url/api/v1/repositories/your-repository-name/queryjobs"

headers = {
    "Authorization": "Bearer your-api-token",
    "Content-Type": "application/json",
    "Accept": "application/json"
}

data = {
    "queryString": "your-query-string",
    "start": "24hours",
    "end": "now",
    "isLive": False
}

response = requests.post(url, headers=headers, data=json.dumps(data))
response_data = response.json()
job_id = response_data.get('id')


import time

url = f"https://your-logscale-url/api/v1/repositories/your-repository-name/queryjobs/{job_id}"

while True:
    response = requests.get(url, headers=headers)
    response_data = response.json()
    if response_data.get('done'):
        break
    time.sleep(1)  # Sleep for 1 second before polling again

events = response_data.get('events')


import pandas as pd

df = pd.DataFrame(events)


import matplotlib.pyplot as plt

plt.hist(df['your-column'], bins=10, edgecolor='black')
plt.title('Histogram of Your Data')
plt.xlabel('Your X Label')
plt.ylabel('Your Y Label')
plt.show()
