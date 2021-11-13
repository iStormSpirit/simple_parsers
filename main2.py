import requests
import fake_useragent
from bs4 import BeautifulSoup

session = requests.Session()
link = "https://ru-forum.com/login.php?action=in"
user = fake_useragent.UserAgent().random


header = {'user-agent': user}

data = {
    'form_sent': '1',
    'req_username': 'qwerty12345_test',
    'req_password': 'qwerty12345'
}

responce = session.post(link, data=data, headers=header)

profile_info = "https://ru-forum.com/login.php"
profile_responce = session.get(profile_info, headers=header).text

cookies_dict = [
    {"domain": key.domain, "name": key.name, "path": key.path, "valuse": key.value}
    for key in session.cookies
]

session2 = requests.Session()

for cookies in cookies_dict:
    session2.cookies.set(**cookies)

resp = session2.get(profile_info, headers=header)
print(resp.text)
