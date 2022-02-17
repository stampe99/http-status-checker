import requests

print('''website http codes:
200 = OK (Regular)
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


