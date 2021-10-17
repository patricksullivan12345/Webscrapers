from bs4 import BeautifulSoup

with open(r"C:\Users\Patrick Sullivan\Desktop\webscraping\Aurora - Colorado Business Entities.html") as fp:
    soup = BeautifulSoup(fp, 'html.parser')

all_rows = soup.find_all('tr')

zip_code = '80014'

zip_list = []
Company_names = []

for row in all_rows:

    if zip_code in str(row):

        zip_list.append(row)

zip_html = BeautifulSoup(str(zip_list[0]), 'html.parser')

for company in zip_list:

    zip_html = BeautifulSoup(str(company), 'html.parser')
    Company_names.append(company.a.text)    

print(Company_names)