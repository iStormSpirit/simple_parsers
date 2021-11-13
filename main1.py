import requests
import fake_useragent
from bs4 import BeautifulSoup

#
# link = "https://icanhazip.com/"
# responce = requests.get(link).content
# print(responce)

# link = "https://browser-info.ru/"
# responce = requests.get(link).text
#
# with open("1.html", "w", encoding="utf-8") as file:
#     file.write(responce)

user = fake_useragent.UserAgent().random
header = {'user-agent': user}


link = "https://browser-info.ru/"
responce = requests.get(link, headers=header).text
soup = BeautifulSoup(responce, 'lxml')
block = soup.find('div', id="tool_padding")

# Check js
check_js = block.find('div', id="javascript_check")
status_js = check_js.find_all('span')[1].text
result_js = f'javascript: {status_js}'

# Check flash
check_flash = block.find('div', id="flash_version")
status_flash = check_flash.find_all('span')[1].text
result_flash = f'flash: {status_flash}'

# Check user-agent
check_user = block.find('div', id="user_agent").text

print(result_js)
print(result_flash)
print(check_user)
