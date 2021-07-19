from bs4 import BeautifulSoup
from selenium import webdriver
import xml.etree.ElementTree as ET
import requests
import time
import json

URL = "https://www.adm.gov.it/portale/monopoli/giochi/giochi_sport/scommesse_fissa/quota-fissa_dove?pr=RM&regione=&rg=lazio&codcom="
json_data = {}
try:
    driver = webdriver.Firefox()
    fileR = open("./resources/codicicomunidiroma.txt",'r')
    for line in fileR:
        URL_SCRAPE = URL+line
        driver.get(URL_SCRAPE)
        time.sleep(2)
        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")
        result = soup.find( "table", {"class":"tabella_d"} )
        xml = ET.fromstring(result.prettify())
        nominal_line = line.replace('\n','')
        json_data[nominal_line] = []
        for child in xml[1]:
            if child[3].text.strip() != 'Indirizzo':
                string_index = child[3].text.replace('Indirizzo', '').strip()
                json_data[nominal_line].append(string_index) 
    with open ("./data.json", "w") as myfile:
        myfile.write(json.dumps(json_data, indent=4))
        myfile.close()
    driver.quit()
    fileR.close()
except :
    driver.quit()
    fileR.close()