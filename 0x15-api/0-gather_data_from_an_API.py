#!/usr/bin/python3
"""returns imfo about user from REST API
"""
if __name__ == "__main__":
    import requests
    import sys
    if isinstance(int(sys.argv[1]), int):
        igr = int(sys.argv[1])
    else:
        igr = int(sys.argv[2])
    url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(igr)
    url2 = 'https://jsonplaceholder.typicode.com/users/{}'.format(igr)
    response = requests.get(url)
    count = 0
    ls = []
    for i in response.json():
        if i.get("completed"):
            count += 1
            ls.append(i.get('title'))

    response2 = requests.get(url2)
    data = response2.json()
    name = data.get('name')
    print("Employee {} is done with tasks({}/20):".format(name, count))
    for i in ls:
        print("\t {}".format(i))
