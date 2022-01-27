import requests
import pandas as pd

URL = 'the api gateway stage invoke url'

data = pd.read_csv('FraudTest.csv', sep = ',', index_col=False)
data_sample = data[:5]

for i in data_sample.index:
    try:
        export = data_sample.loc[i].to_json()

        response = requests.post(URL, data = export)

        print(response)
    except:
        print(data_sample.loc[i])
