#before running this code, ensure that requests and bs4 is installed; check using 'pip freeze'
# pip install bs4 requests

import requests
from bs4 import BeautifulSoup
from csv import writer

# url = 'https://www.amazon.in/gp/product/B07DJHY82F/ref=s9_acss_bw_cg_OP6T_1a1_w?pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-2&pf_rd_r=ZK01ED9497S1DJQYCJY1&pf_rd_t=101&pf_rd_p=9ec4acf8-61c1-4c61-87cf-ff55ae72cfe8&pf_rd_i=15640898031' # OP6t


# url = 'https://www.amazon.in/Cosmic-Purple-128GB-Storage-Offer/dp/B07MDS6JTQ/ref=pd_sbs_107_3?_encoding=UTF8&pd_rd_i=B07MDS6JTQ&pd_rd_r=db8c052c-1c87-11e9-9f02-2dcfb0cd6a52&pd_rd_w=yZCxo&pd_rd_wg=UPvdl&pf_rd_p=9fc668a0-2aac-4fb6-970f-606919bc0185&pf_rd_r=DKX4XXY5XRG7PVANEVT5&psc=1&refRID=DKX4XXY5XRG7PVANEVT5' # oppo r15


#just rerun the code if index out of bounds exception, as sometimes it doesn't hit the link


# url = 'https://amzn.to/2Fz4dI8' #shortened url #oneplus 6t

url = 'https://amzn.to/2Miw2VE' #oppo r15

file_name = 'amazon_oppo_r15_specs.csv'

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

containers = soup.find_all(class_='attrG')

# container = containers[0]     # uncomment this line if you want only specs and no additional info
print("containers = ", containers)

with open(file_name, 'w') as csv_file: # file_name.csv and read/write permissions; will overwrite the exisitng csv each time it's run
    csv_writer = writer(csv_file)
    headers = ['LABEL', 'VALUE'] #comment this line if you don't want headings in csv
    csv_writer.writerow(headers)

    for container in containers:        # comment this line if you want only specs and no additional info, and shift each indentation below to the left
        labels = container.find_all(class_='label')
        print("labels = ", labels)

        values = container.find_all(class_='value')
        print("values = ", values)

        for i in range(max(len(labels), len(values))):
            csv_writer.writerow([labels[i].get_text(), values[i].get_text().replace('\n', '')])

print("Done")


