'''
Web scraping the ASX for ETFs and ETPs with potential.
'''

import asx
import time
from selenium import webdriver
from datetime import datetime

# Python code to convert string to list
def Convert(string):
    li = list(string.split("\n"))
    return li


# path of the chromedriver
PATH = r"/applications/chromedriver"
driver = webdriver.Chrome(PATH)  # to open the browser

a = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
b = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
c = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
d = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]


while (True):
    now = datetime.now()

    # this is just to get the time at the time of
    # web scraping
    current_time = now.strftime("%H:%M:%S")
    print(f'At time : {current_time} ')

    all_shares = []

    for x in range(len(a)):

        for y in range(len(b)):

            for z in range(len(c)):

                for k in range(len(d)):
                    # url of asx request
                    etp_url = f'https://www2.asx.com.au/markets/etp/{a[x]}{b[y]}{c[z]}{d[k]}'

                    # to open the url in the browser
                    driver.get(etp_url)

                    shareInfo_path = f'/html/body/div[1]/div/div[3]/div'

                    # to get that element
                    share = driver.find_element_by_xpath(shareInfo_path)
                    share_item = []
                    share_item.append(Convert(share.text))

                    #exception handling if ticket combination doesn't exist
                    share_object = asx.ASX(' ', ' ', ' ', ' ')
                    try:
                        share_object = asx.ASX(share_item[0][0], share_item[0][2], share_item[0][34], share_item[0][35])
                        print(f"Share: {a[x]}{b[y]}{c[z]}{d[k]}")
                        share_object.format()
                        all_shares.append(share_object)
                        
                    except:
                        continue


    # to stop the running of code for 30 mins
    time.sleep(1200)



