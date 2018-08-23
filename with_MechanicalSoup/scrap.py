import mechanicalsoup
import requests
import re
import json

browser = mechanicalsoup.StatefulBrowser()

bigjson = []
info = {}    
    
def create_json(name,since):
    info['Name'] = name
    info['Friend since'] = since
    
    bigjson.append((info.copy()))

def mech(browser):
    browser.open("http://www.facebook.com/")

    print(browser.get_url())
    browser.follow_link("login")
    print(browser.get_url())
    #print(browser.get_current_page())

    browser.select_form()
    browser["email"] = "EMAIL" #your email
    browser["pass"] = "PASSWORD" #your password

    # Uncomment to launch a real web browser on the current page.
    # browser.launch_browser()

    # Uncomment to display a summary of the filled-in form
    # browser.get_current_form().print_summary()

    response = browser.submit_selected()
    
    
    browser.open("https://web.facebook.com/search/me/friends/females/intersect") 
    print(browser.get_url())
    src = browser.get_current_page()
    src = str(src)


    pattern1 =  re.compile(r"PersonalUser.><span>([\w\s()]*)</span>") #For matching mutual friends Name
    pattern2 =  re.compile(r"[_52eh].>([\w]+\s[\w]+\s[\w]+\s[\w]+\s[\d]+)</div>") #For matching how long youve been friends
    #pattern3 =  re.compile(r"data-hovercard-prefer-more-content-show=.1.>([\w\s()\d]*)</a>") 
    
    
    life1 = re.findall(pattern1, src)
    life2 = re.findall(pattern2, src)
    
    
 
    # Loop through while calling create_json function
    for i,j in zip(life1,life2):
        name = i
        since = j
        create_json(name,since)
    

    # Dumping json into file    
    with open('mech.json','r+') as file:
        json.dump(bigjson,file)
        #l = json.load(file)
        print(l)
    
mech(browser)


