###webscraping train sites
#notes: - need to sort options for multiple suppliers
#       - currently only set to search PECO
#       - GUI would be good at some point
#       - CURR. RETURNING LINKS TO PRODUCTS FROM SEARCH RESULTS

import os
import requests as req
from bs4 import BeautifulSoup as bsoup
from datetime import date


#   Might want to reconsider this bit. What is the purpose of a records folder?
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


###Create URL to results page of selected supplier from user's search term, returning new URL
def create_results_URL(url, query):

    #remove spaces to become query
    for i in query:
        if i == " ":
            i = "+"

    #add query for website to create full search URL
    url += query

    return url


###Find product given URL to results page, returning url of item's page
def find_product(siteURL):

    #gets html data
    page = req.get(siteURL)

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

    return productURL


### ---GET IMAGE---
#go to item page and download image

### ---SELECT SUPPLIER---
#user selects supplier to search correct site
#will act as 'main menu' - more in notes doc.
while menuChoice != "0":
    print("""\nMenu:
          \n1. Peco
          \n2. Gaugemaster
          \n3. Metcalfe
          \n\n0. EXIT""")

    menuChoice = input("Enter: ")

    if menuChoice == "0":
        print("Goodbye")
    else:#this is not good for validation/verification but will work for now
        #select url from library based on menu no.



#MOVE BELOW TO A MENU CHOICE
searchTerm = input("Enter search term: ")













