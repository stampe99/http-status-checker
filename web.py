import requests
from time import sleep

print('''website http codes:
200 = OK (bra)
400 = Bad Request
403 = Forbidden
404 = Not Found
429 = Too Many Requests
502 = Bad Gateway
503 = Service Unavaible
''')

print("========================")

response = requests.get("https://website.domain/")

if response.status_code == 200:
    print(response.status_code)
elif response.status_code == 400:
    print(response.status_code)
elif response.status_code == 403:
    print(response.status_code)
elif response.status_code == 404:
    print(response.status_code)
elif response.status_code == 429:
    print(response.status_code)
elif response.status_code == 502:
    print(response.status_code)
elif response.status_code == 503:
    print(response.status_code)
else:
    print("http code not defined")

user_input = input("Do you want to check the website status repeatedly? (This may cause lag on low-end devices), (Y/N)\n")
if user_input == "y".lower():
    print("Starting now... 3. 2. 1. ")
    sleep(3)
    while True:
        for i in range(1000):
            print(i, response.status_code)
elif user_input == "n".lower():
    quit()
