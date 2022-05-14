from bs4 import BeautifulSoup as soup
import requests
import csv
from time import sleep
from random import randint
import urllib
import pandas as pd

def delay() -> None:
    sleep(randint(2,5))
    return None


def main():
    def prepend(list, str):
       
    # Using format()
    str += '{0}'
    list = [str.format(i) for i in list]
    return(list)

    URL = "https://www.stepstone.de/5/ergebnisliste.html?what=Data%20Science&suid=96864f5c-62c5-4152-9c2a-bc771d184484&of={}"
    pagenumber= = {0,1,2,3,4,5}
    mylist = []
    for number in pagenumber:
        source = requests.get(URL.format(number))
        delay()
        jobs = soup(source.content, "html.parser")
        cont = jobs.find_all("a", class_="sc-pAZqv cyGFEN")
        for names in cont:
            refs = names.get("href")
            mylist.append(refs)
        
        list = mylist
        str = 'https://www.stepstone.de/'
        mylist_new = prepend(list,str)
        
    comp_name = [] 
    for comps in jobs.find_all("div", class_="sc-pIJJz cqcAcN"):
        delay()
        name1 = comps.text
        comp_name.append(name1)
        
    
    job_title = []
    for title in jobs.find_all("h2", class_="sc-pJurq hXakmZ"):
        delay()
        tit = title.text
        job_title.append(tit)
        
        
    anfo = []
    for urlZ in urls1:
    delay()
    r = requests.get(urlZ)
    detailed_soup = soup(r.content, "html.parser")

        for reqs in detailed_soup.find_all("div", class_="at-section-text-description-content listingContentBrandingColor sc-iELTvK duaMgn"):
            req = reqs.text
            anfo.append(req)
    
    
    
    lst_tit = [job_title[i:i+1] for i in range(0, len(job_title), 1)]  
    lst_url = [mylist_new[i:i+1] for i in range(0, len(mylist_new), 1)]  
    lst_name = [comp_l[i:i+1] for i in range(0, len(comp_name), 1)] 
    lst_anfo = [anfo[i:i+1] for i in range(0, len(anfo), 1)]
    
    
    
    df = pd.DataFrame()
    df["Company_Name"] = lst_name
    df["title"] = lst_tit
    df["url"] = lst_url
    df["reqs"] = lst_anfo
    df['Company_Name'] = df['Company_Name'].str[0]
    df['title'] = df['title'].str[0]
    df['url'] = df['url'].str[0]
    df["reqs"] = df["reqs"].str[0]
    df= df.replace(r'\n',' ', regex=True)
    
    
    df.to_csv("test_scrape.csv",
    return(df)
    



    
    