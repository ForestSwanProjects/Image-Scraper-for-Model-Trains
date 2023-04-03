###downloading image from webpage to folder + file reduction

import os
import requests as req
from bs4 import BeautifulSoup as bsoup

url = "https://www.gaugemasterretail.com/catalogsearch/result/?q=box+van"
page = req.get(url)
htmlData = page.text
soup = bsoup(htmlData, "html.parser")
for i in soup.find_all("img"):
    print(i["src"])

print("")
