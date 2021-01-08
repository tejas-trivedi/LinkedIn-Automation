from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import pandas

colname = ['names']
data = pandas.read_excel('math_names.xlsx', names=colname, sheet_name="Sheet1")
all_names = data.names.tolist()

length = len(all_names)

options = Options()
options.add_argument('--headless')
browser = webdriver.Chrome(options=options)
numbers = []

for i in range(length):
    #Open login page
    browser.get('https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin')
    
    #Enter login info:
    elementID = browser.find_element_by_id('username')
    #print("entering username...")
    elementID.send_keys('your_username')

    #print("entering password...")
    elementID = browser.find_element_by_id('password')          #Note: replace the keys "your_username" and "your_password" with your LinkedIn login info
    elementID.send_keys('your_password')
    #print("submitting...")
    elementID.submit()
    #print("submitted")

    browser.get('https://www.linkedin.com/feed/?trk=guest_homepage-basic_nav-header-signin')
    search_query = browser.find_element_by_class_name('search-global-typeahead__input')
    search_query.send_keys(all_names[i]) 
    search_query.send_keys(Keys.RETURN)

    time.sleep(10)
    print(all_names[i])
    print("done searching")
    people = browser.find_element_by_class_name("search-reusables__filter-pill-button").click()
    time.sleep(10)
    try:
        number = browser.find_element_by_xpath("//*[@class='pb2 t-black--light t-14']").text
    except:
        number = "None"

    numbers.append(number)
    print(all_names[i], number)

print(numbers)

dict = {'name': all_names, 'number': numbers} 
df = pandas.DataFrame(dict) 
df.to_csv('name_num.csv')  

print("Done with all names")