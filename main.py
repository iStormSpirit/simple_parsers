import json
import requests
from bs4 import BeautifulSoup


def get_js(sp):
    block = sp.find('div', id='javascript_check')
    print(block.find_all('span')[1].text)


def get_cookie(sp):
    block = sp.find('div', id='cookie_check')
    print(block.find_all('span')[1].text)


def get_flash(sp):
    block = sp.find('div', id='flash_version')
    print(block.find_all('span')[1].text)


def main():
    with open('config.json') as file:
        config = json.load(file)

    responce = requests.get("https://browser-info.ru/").text
    soup = BeautifulSoup(responce, 'lxml')

    if config['js'] == True: get_js(soup)
    if config['cookie'] == True: get_cookie(soup)
    if config['flash'] == True: get_flash(soup)


if __name__ == '__main__':
    main()
