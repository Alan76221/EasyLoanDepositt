import requests 
from bs4 import BeautifulSoup 

URL = "https://www.creditkarma.com/reviews/personal-loan/single/id/BestEgg"
r = requests.get(URL) 
soup = BeautifulSoup(r.content, 'html5lib') 
print(soup.prettify()) 
table = soup.find('p')
print(table) 
