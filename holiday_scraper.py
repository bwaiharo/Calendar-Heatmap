import json
from bs4 import BeautifulSoup
import requests
from splinter import Browser
import pandas as pd
from pprint import pprint
import re
from random import randint
from time import sleep
import datetime
year = datetime.date.today().year

countries  = ["afghanistan", "albania", "algeria", "american-samoa", "andorra", 
"angola", "anguilla", "antigua-and-barbuda", "argentina", "armenia", 
"aruba", "australia", "austria", "azerbaijan", "bahrain", "bangladesh", 
"barbados", "belarus", "belgium", "belize", "benin", "bermuda", "bhutan", 
"bolivia", "bosnia", "botswana", "brazil", "british-virgin-islands", "brunei", 
"bulgaria", "burkina-faso", "burundi", "cape-verde", "cambodia", "cameroon", "canada", 
"cayman-islands", "central-african-republic", "chad", "chile", "china", "colombia", "comores", 
"republic-of-the-congo", "dr-congo", "cook-islands", "costa-rica", "ivory-coast", "croatia", "cuba", 
"curacao", "cyprus", "czech", "denmark", "djibouti", "dominica", "dominican-republic", "timor-leste", 
"ecuador", "egypt", "el-salvador", "guineaecuatorial", "eritrea", "estonia", "swaziland", "ethiopia", 
"falkland-islands", "faroe-islands", "fiji", "finland", "france", "french-guiana", "french-polynesia", 
"gabon", "gambia", "georgia", "germany", "ghana", "gibraltar", "greece", "greenland", "grenada", 
"guadeloupe", "guam", "guatemala", "guernsey", "guinea", "guinea-bissau", "guyana", "haiti", 
"honduras", "hong-kong", "hungary", "iceland", "india", "indonesia", "iran", "iraq", "ireland", 
"isle-of-man", "israel", "italy", "jamaica", "japan", "jersey", "jordan", "kazakhstan", "kenya", 
"kiribati", "kosovo", "kuwait", "kyrgyzstan", "laos", "latvia", "lebanon", "lesotho", "liberia", 
"libya", "liechtenstein", "lithuania", "luxembourg", "macau", "madagascar", "malawi", "malaysia", 
"maldives", "mali", "malta", "marshall-islands", "martinique", "mauritania", "mauritius", "mayotte", 
"mexico", "micronesia", "moldova", "monaco", "mongolia", "montenegro", "montserrat", "morocco", "mozambique", 
"myanmar", "namibia", "nauru", "nepal", "netherlands", "new-caledonia", "new-zealand", "nicaragua", "niger", "nigeria", 
"north-korea", "macedonia", "northern-mariana-islands", "norway", "oman", "pakistan", "palau", "panama", "papua-new-guinea", 
"paraguay", "peru", "philippines", "poland", "portugal", "puerto-rico", "qatar", "reunion", "romania", "russia", "rwanda", 
"saint-helena", "saint-kitts-and-nevis", "saint-lucia", "saint-martin", "saint-pierre-and-miquelon", "saint-vincent-and-the-grenadines", 
"samoa", "san-marino", "sao-tome-and-principe", "saudi-arabia", "senegal", "serbia", "seychelles", "sierra-leone", "singapore", "sint-maarten", 
"slovakia", "slovenia", "solomon-islands", "somalia", "south-africa", "south-korea", "south-sudan", "spain", "sri-lanka", "saint-barthelemy", "sudan", 
"suriname", "sweden", "switzerland", "syria", "taiwan", "tajikistan", "tanzania", "thailand", "bahamas", "togo", "tonga", "trinidad", "tunisia", "turkey", 
"turkmenistan", "turks-and-caicos-islands", "tuvalu", "uganda", "ukraine", "united-arab-emirates", "uk", "us", "uruguay", "united-states-virgin-islands", 
"uzbekistan", "vanuatu", "vatican-city-state", "venezuela", "vietnam", "wallis-and-futuna", "yemen", "zambia", "zimbabwe"]

# countries  = ["aruba", "australia"]

def scrape_holidays():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "chromedriver.exe"}
    browser = Browser("chrome", **executable_path, headless=True)
    # holi_list = list()
    holi = dict()
    for ct in countries:
        sleep(randint(10,100))
        # Let's get the JSON for 100 posts sequentially.
        url = f'https://www.timeanddate.com/holidays/{ct}'
        tables = pd.read_html(url)
        
        df = tables[0]
        cols = len(df.columns)
        if (cols == 4):
            df.columns = ['Date','Day', 'Name', 'Type']
            df['Year']= str(year)
            df['Country']= ct
            df = df.dropna()
        else:
            df.columns = ['Date','Day', 'Name', 'Type','Details']
            df['Year']= str(year)
            df['Country']= ct
            df = df.dropna()
    #     holi_list.append(df.to_dict(orient='records'))
        holi[str(ct)] = df.to_dict(orient='records')
    return holi
