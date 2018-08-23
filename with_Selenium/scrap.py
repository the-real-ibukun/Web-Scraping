import re
import requests
import time
from selenium import webdriver
import json

chrome = webdriver.Chrome()

# USING REGEX WITH SELENIUM
def get_facesel(chrome):
    chrome.get('http://www.facebook.com/login')
    email = chrome.find_element_by_id('email')
    email.send_keys('EMAIL')
    
    pass1 = chrome.find_element_by_id('pass')
    pass1.send_keys('PASSWORD')
    email.submit()

    chrome.get('https://web.facebook.com/search/me/friends/females/intersect')
    
    
    src = chrome.page_source
    
    pattern =  re.compile(r"PersonalUser.><span>([\w\s()]*)</span>|[_52eh].>([\w\s()\d]+)</div>|data-hovercard-prefer-more-content-show=.1.>([\w\s()\d]*)</a>") 
    life = re.findall(pattern, src)

    print(life)
    
#get_facesel(chrome)


bigjson = []
info = {} 
def create_json(name, other_info):
    bigjson = []
    info = {}

    bigjson.append(info.copy())

# USING XPATH WITH SELENIUM
def xpat_sel(chrome):
    chrome.get('http://www.facebook.com/login')

    email = chrome.find_element_by_id('email')
    email.send_keys('EMAIL') # Your email
    
    pass1 = chrome.find_element_by_id('pass')
    pass1.send_keys('PASSWORD') # Your password
    email.submit()

    # Retrieving browser cookies
    cookies_list = chrome.get_cookies()
    cookies_dict = []
    for cookie in cookies_list:
        cookies_dict.append([cookie['name'],cookie['value']])
    with open('log.json','r') as file:
        json.dump(cookies_dict,file) 
        #json.load(file)
   

    chrome.get('https://web.facebook.com/search/me/friends/females/intersect')
    
    p = chrome.find_elements_by_xpath('//*[@*]/div/div[2]/div/div[1]/div[2]/div/div/div/a/span') # Mutual friend name
        
    pl = chrome.find_elements_by_xpath('//*[@*]/div/div[2]/div/div[2]/div[2]/div') # Mutual friend since
    

    # Loop through while calling create_json function
    for i,j in zip(p,pl):
        name = i
        other_info = j
        create_json(name, other_info)

    # Dumping json into file    
    with open('sel.json','r+') as file:
        json.dump(bigjson,file)
        #l = json.load(file)
        print(l)
        
xpat_sel(chrome)



 