from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--headless')
browser = webdriver.Chrome(options=options)

#Open login page
browser.get('https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin')

#Enter login info:
elementID = browser.find_element_by_id('username')
print("entering username...")
elementID.send_keys('your_username')

print("entering password...")
elementID = browser.find_element_by_id('password')          #Note: replace the keys "your_username" and "your_password" with your LinkedIn login info
elementID.send_keys('your_password')
print("submitting...")
elementID.submit()
print("submitted")

search_query = browser.find_element_by_class_name('search-global-typeahead__input')
search_query.send_keys("Name you want to search")               # Type the persons name to check number of people with that name on LinkedIn
search_query.send_keys(Keys.RETURN)

time.sleep(10)
print("done searching")
people = browser.find_element_by_class_name("search-reusables__filter-pill-button").click()
time.sleep(10)
print("Finding number of people with the given name")
number = browser.find_element_by_xpath("//*[@class='pb2 t-black--light t-14']").text
print(number)

