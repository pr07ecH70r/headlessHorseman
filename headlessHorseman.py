#===Main idea: Requests gets the page; BS4 parses the data===

#===IMPORTS===

import requests
from bs4 import BeautifulSoup
import time

#===GLOBALS===
url = input("Enter page URL: ") #The page url that will be scrapped
page = ''

#===Implementing a connection error back-up plan
while page == '':
    try:
        page = requests.get(url) #Requests get method for obtaining the data
        break
    except:
        print("Connection refused by the server...")
        print("Implementing a delay...")
        secs = input(int("Delay = "))
        time.sleep(secs)
        continue

data = page.text #Gets the data as text

source = BeautifulSoup(data, "html.parser") #Converts data to var BS4 object
pretty_source = source.prettify() #BS4 Prettify method on source var

#===DATA TO FILE===
local_file = open("D:\Python test central\Headless horseman\Scrap1.txt", "w")
#local_file = open(url.strip("https://" + "http://") + "_scrapped.txt", "w") #Opens source in write mode to var local_file

#local_file.write(pretty_source) #Creates a new file & writes the var pretty_soup to file

#===ENCODING ISSUES HANDLE===
local_file.write(str(pretty_source.encode('utf-8')))
local_file.close() #Close file