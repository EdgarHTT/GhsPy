import requests
from bs4 import BeautifulSoup

req = requests.get("https://pubchem.ncbi.nlm.nih.gov/compound/2244#section=Safety-and-Hazards")

soup= BeautifulSoup(req.text)

print(soup)