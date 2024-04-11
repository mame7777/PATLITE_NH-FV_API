import urllib.request
import json

# "IP"と"PORT"を環境に合わせて変更する
url = "http://IP:PORT/api/lights_buzer/"

def post(num):
    num += "9"
    req = urllib.request.Request(url=url + num, method="POST")
    try:
        with urllib.request.urlopen(req) as response:  
            response_body = response.read().decode("utf-8")
            print(response_body)
    except urllib.error.HTTPError as e:
        print(e)

def main():
    while True:
        for i in reversed(range(6)):
            for j in range(i):
                num = "0"*i+"1"*(5-i)
                num = num[:j] + "1" + num[j+1:]
                post(num)
        
if __name__ == "__main__":
    main()