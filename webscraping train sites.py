###webscraping train sites
#notes: - need to sort options for multiple suppliers
#       - currently only set to search PECO
#       - GUI would be good at some point
#       - CURR. RETURNING LINKS TO PRODUCTS FROM SEARCH RESULTS

import os
import requests as req
from bs4 import BeautifulSoup as bsoup
from datetime import date


### ---FILE ORGANISATION---
#NOTES: - file labelling needs refining but works for now
#       - files only being created, nothing being written yet

#determining how many files in records folder
n = 0
recordsDir = "C:\\Users\\44776\\Python\\Images for Products from Website\\train site results"
recordsList = os.listdir(recordsDir)

for i in range(len(recordsList)):
    n += 1

n += 1

#determining date
today = date.today()

#determine where we store files
savePath = "C:\\Users\\44776\\Python\\Images for Products from Website\\train site results"

#creating file name and ensuring it's stored in right place
filename = "records_" + str(today) + "_" + str(n) + ".txt"
completeName = os.path.join(savePath, filename)

#creating file
f = open(completeName, "x")
f.close()

#open file for writing
records = open(completeName, "a")


### ---INPUT SEARCH TERM---
#put before file org. and incorporate into file name??

searchTerm = input("Enter search term: ")

#turn spaces to +'s to create query
query = searchTerm

for i in query:
    if i == " ":
        i = "+"

#add search term as query for website to create URL
url = "https://peco-uk.com/search?q=" + query


### ---WEBSCRAPING TO FIND PRODUCT---
#returns top 3 results, user selects correct one, go to that link then get image
#NOTES: - returning product links
#       - look at 'images to folder with reduction.py' for next bit

#gets html data
page = req.get(url)

#use appropriate parser
soup = bsoup(page.content, "html.parser")

#results container
siteResults = soup.find(class_="result-rows")

#elements in results container
resultsElements = siteResults.find_all("div", class_="search--items")
#print(resultsElements)

#cycle through results, print name of first 3 results
for j in range(3):
    currEl = resultsElements[j]
    productName = currEl.find("a").getText()
    print(str(j+1) + ": " + productName)

#VALIDATION/VERIFICATION REQUIRED
userChoice = int(input("Enter number corresponding to correct item: "))
productURL = resultsElements[userChoice-1].find("a").get("href")

print(productURL)
print(" ");














