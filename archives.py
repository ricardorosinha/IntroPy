# 1 - Import libraries/packages
import json

# 2 - Classes


# 3 - Definitions (Functions and Methods)

data = {}

data['client'] = [] # creation of and array []
data['client'].append(
    {
     'name':'Ricardo',
     'phone':'351000000000',
     'email':'ricardo@mail.com'
     }
)

data['client'].append(
    {
     'name':'Paula',
     'phone':'352000000000',
     'email':'paula@mail.com'
     }
)


def create_json():
    with open('client.json','w') as outfile:
        json.dump(data,outfile)


def read_json():
    with open('client2.json') as outfile:
        data = json.load(outfile)
        for register in data['clients2']:
            print('name: ' + register['name'])
            print('phone: ' + register['phone'])
            print('e-mail: ' + register['email'])
            print(' ')


def test_create_json():
    create_json()
    print(data['client'])


def test_read_json():
    read_json()