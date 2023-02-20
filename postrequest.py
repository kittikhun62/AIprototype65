import requests
import json

if __name__ == "__main__":

    url = 'http://10.71.160.33:5001/postrequest'
    myobj = {'kittikhun': 'kiattisaksiri'}

    x = requests.post(url, data = json.dumps(myobj))

    print(x.text)