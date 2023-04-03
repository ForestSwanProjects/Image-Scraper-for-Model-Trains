###downloading image from webpage to folder + file reduction

import os
import requests as req
from bs4 import BeautifulSoup as bsoup

url = "https://www.gaugemasterretail.com/catalogsearch/result/?q=box+van"
page = req.get(url)
htmlData = page.text
soup = bsoup(htmlData, "html.parser")
for i in soup.find_all("img"):
    #print(i["src"])
    #below copied from https://www.youtube.com/watch?v=stIxEKR7o-c at 8:32
    name = i["alt"]
    link = i["src"]
    fileName = name.replace(" ", "-").replace("/", "-").replace("*", "") + ".jpg"
    with open(fileName, "wb") as f:
        img = req.get(link)
        f.write(img.content)

print("")

