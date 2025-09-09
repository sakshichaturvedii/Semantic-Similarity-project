import requests
import pandas as pd

url = "http://127.0.0.1:5000/similarity"

df = pd.read_csv("DataNeuron_Text_Similarity.csv")  

for i, row in df.head(5).iterrows():
    text1 = row["text1"]
    text2 = row["text2"]

    payload = {"text1": text1, "text2": text2}
    response = requests.post(url, json=payload)

    if response.status_code == 200:
        print(f"Row {i} → {response.json()}")
    else:
        print(f"Row {i} → Error {response.status_code}")
