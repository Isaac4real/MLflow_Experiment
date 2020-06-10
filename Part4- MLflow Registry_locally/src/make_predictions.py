import requests
from cls.utils import Utils
import json

(x_train, y_train), (val_x, val_y) = Utils.load_data()

data = val_x[0].reshape(1, -1)
data_json = json.dumps(data.tolist())
# print(data_json)
headers = {'Content-Type': 'application/json; format=pandas-records'}
request_uri = 'http://127.0.0.1:5000/invocations'

if __name__ == '__main__':
    try:
        response = requests.post(request_uri, data=data_json, headers=headers)
        print(response.content)
        print('done!!!')
    except Exception as ex:
        raise (ex)
