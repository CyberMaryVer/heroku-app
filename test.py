import requests
import json
import pandas as pd

loaded_df = pd.read_csv('dataset_test.csv')
X_test, y_test = loaded_df.iloc[:, :-1], loaded_df.iloc[:, -1]
value_to_predict = [list(X_test.iloc[1].values)]
values_to_predict = X_test.iloc[1:8]

def test_one_sample(x=value_to_predict, url = 'http://localhost:5000/predict/'):
    j_data = json.dumps(x)
    headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
    r = requests.post(url, data=j_data, headers=headers)
    print(f"Prediction: {r.text}")

def test_many_samples_one_by_one(x=values_to_predict, url = 'http://localhost:5000/predict/'):
    data1= [[list(row)] for row in x.values]
    data2 = x.index
    # data = [list(X_test.iloc[1].values)]

    print('Getting predictions...')
    for sample, idx in zip(data1, data2):
        j_data = json.dumps(sample)
        headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
        r = requests.post(url, data=j_data, headers=headers)
        print(f'Prediction for sample #{idx}: {r.text}')

def test_many_samples_together(x=values_to_predict, url = 'http://localhost:5000/predictm/'):
    data= [list(row) for row in x.values]
    j_data = json.dumps(data)
    headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
    r = requests.post(url, data=j_data, headers=headers)
    pred = json.loads(r.text)
    # print(type(pred))
    print(f"Prediction: {pred}")

# test_one_sample()

test_many_samples_together(url='https://mytest0000.herokuapp.com/predictm/')