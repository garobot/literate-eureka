# Request Api 
# pip install requests
import requests
# Get Data
headers = {
    "Connection": "keep-alive",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"
}
r = requests.get('https://api.example.com', headers=headers)
print(r.status_code) # 200
print(r.headers['content-type'])
print(r.content) # HTML Data
# Login Site
payload = {'username': 'USERNAME', 'userpass': 'PASSWORD'}
r = requests.post('https://example.com/login', data=payload)
print(r.status_code) # 200