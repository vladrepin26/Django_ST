import json

import requests as req

data01 = {'brokerQuery':
              {'CompanyId': '02655916',
               'LegId': '',
               'CarrierCode': '',
               'Date': '07/22/2018 4:00:00 AM',
               'Status': 3
               }
          }

temp = json.dumps(data01, ensure_ascii=False)

url = 'http://192.168.0.172:8081/broker/getdispatch'
headers = {'Content-Type': 'application/json'}

response = req.post(url, data=temp, headers=headers).json()

print(response['Value'][0])

# python_dict = json.loads(response['Value'])
# python_dict[0]

# print(python_dict[0]['Client']['LastName'],
#       python_dict[0]['Client']['FirstName'],
#       python_dict[0]['PickUpTimeStr'],
#       python_dict[0]['AddressFrom']['Street'],
#       python_dict[0]['AddressFrom']['City'],
#       python_dict[0]['AddressTo']['Street'],
#       python_dict[0]['AddressTo']['City'])
