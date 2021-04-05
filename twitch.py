import requests

url = "http://www.google.com"

payload = "user=mridul&clientId=%3CREQUIRED%3E"
headers = {
    'content-type': "application/x-www-form-urlencoded",
    'x-rapidapi-key': "0e2d98e4f8msh4ffd385a24cfdefp15cb76jsn6ebc06bcc143",
    'x-rapidapi-host': "146.148.98.174:8080"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)