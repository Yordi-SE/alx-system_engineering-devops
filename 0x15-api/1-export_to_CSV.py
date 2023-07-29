#!/usr/bin/python3
"""returns imfo about user from REST API
"""
if __name__ == "__main__":
    import sys
    import csv
    import requests
    if isinstance(int(sys.argv[1]), int):
        igr = int(sys.argv[1])
    else:
        igr = int(sys.argv[2])
    url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(igr)
    url2 = 'https://jsonplaceholder.typicode.com/users/{}'.format(igr)
    response = requests.get(url)
    response2 = requests.get(url2)
    data = response2.json()
    username = data.get('username')
    user_id = data.get('id')
    with open("{}.csv".format(igr), 'a', encoding='utf-8') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for i in response.json():
            data2 = [[user_id, username, i.get('completed'), i.get('title')]]
            writer.writerows(data2)
