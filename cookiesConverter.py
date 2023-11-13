import json

datas = []

with open('Data.txt', 'r') as file:

    for i in file:
        datas.append(i.rstrip())

rc = []
for i in datas:
    cookies = json.loads(i.split('|')[-1])

    at = ''
    ct0 = ''
    for p in cookies:
        if p['name'] == 'auth_token':
            at = p['value']
        if p['name'] == 'ct0':
            ct0 = p['value']

    rc.append(f'auth_token={at}; ct0={ct0}')

with open('ReadyData.txt', 'w+') as file:
    for i in rc:
        file.write(i+'\n')

