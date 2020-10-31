from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path=r'C:\Users\user\Desktop\sellenium\chromedriver.exe')

blue = 'https://bluepartner.eu/pl/kontakt/'
driver.get(blue)

adress = driver.current_url
print(adress)
if adress != blue:
    exit(1)

#imie i nazwisko
imie = driver.find_element_by_id("id_imie-i-nazwisko")
imie.send_keys("CloudServices Test")
time.sleep(1)

#email
email = driver.find_element_by_id("id_e-mail")
email.send_keys('quen1965@armyspy.com')
time.sleep(1)

#wybierz temat
dropdown = Select(driver.find_element_by_id("id_wybierz-temat"))
dropdown.select_by_index(2)
time.sleep(1)

#treść
tresc = driver.find_element_by_id("id_tresc")
tresc.send_keys("automat test CloudServices")
time.sleep(1)

driver.execute_script("window.scrollTo(0, 300)") #wymagane by ominąć iframe, który przykrywa checkbox, który trzeba zaznaczyć

#zgoda
zgoda = driver.find_element_by_css_selector("[id*='id_wyra']")
#checkbox_zgoda.click()

act = ActionChains(driver)
act.move_to_element(zgoda).click(zgoda).perform()
time.sleep(1)

#wyślij
form = driver.find_element_by_class_name('form-horizontal')
form.submit()
time.sleep(3)

