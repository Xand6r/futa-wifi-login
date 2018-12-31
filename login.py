from selenium import webdriver
import sys
browser=webdriver.Chrome(r"C:/chromedriver.exe")
browser.get("http://futa.internal/login")


logins={'username':"liogunleye@futa.edu.ng"],
        'password':[19960082]}    

for username,password in zip(logins['username'],logins['password']):
        text="server"
        while 'erver' in text or "assword" in text:
                user_slot = browser.find_element_by_xpath("/html/body/header/nav/div/div/div/div[2]/form/input[3]")
                password_slot = browser.find_element_by_xpath("/html/body/header/nav/div/div/div/div[2]/form/input[4]")
                button=browser.find_element_by_xpath("/html/body/header/nav/div/div/div/div[2]/form/button")

                user_slot.clear()
                user_slot.send_keys(username)
                password_slot.send_keys(password)
                button.click()

                title=browser.title
                if 'tatus' in title:
                        browser.close()
                        sys.exit()
                text=browser.find_element_by_xpath("/html/body/header/nav/div/div/div/div[2]/div").text

