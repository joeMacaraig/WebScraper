from bs4 import BeautifulSoup
import requests
import re

searching = input("What product do you want to search for?") #cpu, gpu, desktop, mouse, webcam

url = f'https://www.newegg.com/p/pl?d={searching}&N=4131' #in stock, removing &N.... will give you all
page = requests.get(url).text
doc = BeautifulSoup(page, "lxml") 

#Query Pages
page_text = doc.find(class_="list-tool-pagination-text").strong
pages = int(str(page_text).split("/")[-2].split(">")[-1][:-1])
print(pages) 

for page in range(1, pages + 1):
    url = f'https://www.newegg.com/p/pl?d={getting}&N=4131&page={page}' # 
    page = requests.get(url).text
    doc = BeautifulSoup(page, "lxml") 
    
    itemReturn = doc.find_all(text=re.compile(searching)) #.compile returns anything with the search 13 min