import requests
from bs4 import BeautifulSoup

r=requests.get("placeholder")
c=r.content

soup=BeautifulSoup c, "html.parser"
