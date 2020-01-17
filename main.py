from selenium import webdriver
import os
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

chromedriver = "D:/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)

def goto(url):
    driver.get(url)
    time.sleep(1.5)

class InstagramBot:
    def __init__(self, email, password):
        self.email = email
        self.password = password

    def login(self):
        goto("https://www.instagram.com/")
        # Login element
        login = driver.find_element_by_xpath("//*[@id='react-root']/section/main/article/div[2]/div[2]/p/a")
        login.click()
        time.sleep(2)

        username = driver.find_element_by_name("username")
        username.send_keys(self.email)

        password = driver.find_element_by_name("password")
        password.send_keys(self.password)

        # Logging in Instagram through our password and surname which is saved under loginInfo.py file.
        login_button = driver.find_element_by_xpath(
            "/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[4]/button")
        login_button.click()
        time.sleep(2)

    def follow(self,count):
        goto("https://www.instagram.com/explore/people/suggested/")
        counts=0
        while counts<count:
            try:
                buttons=driver.find_elements_by_css_selector("button")
                for button in buttons :
                    if (button.text == "Follow") and (counts<count):
                        button.click()
                        time.sleep(0.5)
                        counts+=1
                driver.find_element_by_tag_name('body').send_keys(Keys.END)
                time.sleep(4)
            except Exception as e:
                print(e)

    def unfollow(self,count):
        goto(str("https://www.instagram.com/"+str(self.email)+"/"))
        counts=0
        while counts<count:
            try:
                buttons=driver.find_elements_by_css_selector("button")
                for button in buttons :
                    if (button.text == "Following") and (counts<count):
                        button.click()
                        time.sleep(0.5)
                        temp_button=driver.find_elements_by_css_selector("button")
                        for temps_button in temp_button:
                            if temps_button.text=="Unfollow":
                                temps_button.click()
                                time.sleep(0.5)
                                counts+=1
                                break
                driver.find_element_by_tag_name('body').send_keys(Keys.END)
                time.sleep(4)
            except Exception as e:
                print(e)



i=InstagramBot(email="########",password="##########")
i.login()
i.unfollow(count=20)
