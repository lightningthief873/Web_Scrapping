import encodings
from lib2to3.pgen2.token import NEWLINE
import requests
from bs4 import BeautifulSoup
from csv import writer

url = "my_url"

page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

lists = soup.find_all('div', class_="result_container")

with open('My_file_name.csv', 'w', encoding='utf8', newline='') as f:
    thewriter = writer(f)
    header = ['Name', 'Location', 'Owner', 'Contact']
    thewriter.writerow(header)
    for list in lists:
        name = list.find('div', class_="result_container--right-title").text.replace('\n', '')
        location = list.find('div', class_="result_container--right-location").text.replace('\n', '')
        owner = list.find('div', class_="result_container--right-contactname").text.replace('\n', '')
        contact = list.find('div', class_="result_container--right-contactno").text.replace('\n', '')
        info = [name, location, owner, contact]
        thewriter.writerow(info)




