import requests
from bs4 import BeautifulSoup

# Retrieve newest URL
Sciensano_url = 'https://epistat.wiv-isp.be/covid/'
requestSciensano = requests.get(Sciensano_url)
soup = BeautifulSoup(requestSciensano.content)
allListItems = list(soup.find_all("li"))
latestListItem = [item for item in allListItems if str(item).__contains__("Complete dataset")][0]
datasetLoc = latestListItem.find("a").get("href")

# Download xlsx
resp = requests.get(datasetLoc)
fileLoc = './Raw/COVID19BE_Source.xlsx'
output = open(fileLoc, 'wb')
output.write(resp.content)
output.close()
