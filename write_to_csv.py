import requests
from bs4 import BeautifulSoup
import csv

page_link='C:/Users/dhimam/Desktop/GitWork/WebScraping/Myfile.html'

f = open(page_link, 'r')
s = f.read()
soup = BeautifulSoup(s,"html.parser")

title=soup.find('title')
print(title.text)

element_list=[]
for element in soup.find_all('li'):
    element_list.append(element.text)

print(element_list)

with open("web_out.csv",'w') as outfile:
    for item in element_list:
        outfile.write(item+" ")

