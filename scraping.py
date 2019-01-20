import requests
from bs4 import BeautifulSoup
from csv import writer

response = requests.get('https://iiita.ac.in')

soup = BeautifulSoup(response.text, 'html.parser')

containers = soup.find_all(class_='row')

with open('posts.csv', 'w') as csv_file:
    csv_writer = writer(csv_file)
    headers = ['Links', 'Headings in Sidebar']
    csv_writer.writerow(headers)

    for container in containers:
        # print(container.get_text().replace('\n', ''))
        # print("=========================")

        # getting the links
        link = container.find('a')['href']
        # print(link)
        # print('----------')

        #getting all headings in sidebar
        
        headings_sidebar = soup.find_all(id='rside_bar')
        # for headings in headings_sidebar:
        #     print(headings.get_text())
        csv_writer.writerow([link, headings_sidebar[i++].get_text()])