import re
from bs4 import BeautifulSoup as bs

from robobrowser import RoboBrowser

br = RoboBrowser()
br.open("https://cashneon.com/login")
form = br.get_form()
form['phone'] = int('2626729101')
form['ssn'] = int('5808')
br.submit_form(form)
soup = br.parsed
print(soup.text)


