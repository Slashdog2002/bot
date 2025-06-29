from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

class InstagramBot:
    def __init__(self):
        self.service = Service("C:\\Users\\ansuj\\OneDrive\\Desktop\\chromedriver-win64\\chromedriver.exe")
        self.driver = webdriver.Chrome(service=self.service)
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)
        
        #Accountdaten
        self.username = "zitate.stan"
        self.password = "FreibergAmNeckar2002"
        self.target_account = "Zitate.stan"

    def accept_cookies(self):
        try:
            cookie_btn = self.wait.until(EC.element_to_be_clickable(
                (By.XPATH, "/html/body/div[3]/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[1]")))
            cookie_btn.click()
            print("Cookies accepted")
        except Exception as e:
            print(f"Cookie acceptance failed: {str(e)}")

    def login(self):
        try:
            #Website Instagram aufrufen
            self.driver.get("https://www.instagram.com/")
            time.sleep(2)
            
            #Cookies akzeptieren
            self.accept_cookies()
            
            #Benutzername eingeben
            username_field = self.wait.until(EC.presence_of_element_located(
                (By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div/section/main/article/div[2]/div[1]/div[2]/div/form/div[1]/div[1]/div/label/input")))
            username_field.send_keys(self.username)
            
            #Passwort eingeben
            password_field = self.driver.find_element(By.XPATH,
                "/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div/section/main/article/div[2]/div[1]/div[2]/div/form/div[1]/div[2]/div/label/input")
            password_field.send_keys(self.password)
            
            #"Anmelden" Button klciken
            login_button = self.driver.find_element(By.XPATH,
                "/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div/section/main/article/div[2]/div[1]/div[2]/div/form/div[1]/div[3]/button")
            login_button.click()
            print("Login successful")
            
            time.sleep(5)
            
        except Exception as e:
            print(f"Login failed: {str(e)}")
            self.quit()

    def navigate_to_target_account(self):
        try:
            #Suche Button geklickt
            search_btn = self.wait.until(EC.element_to_be_clickable(
                (By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div[2]/div[2]/span")))
            search_btn.click()
            time.sleep(2)
            
            #Account Name eingeben
            search_field = self.driver.find_element(By.XPATH,
                "/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div[2]/div/div/div/div[2]/div/div/div[1]/div/div/input")
            search_field.send_keys(self.target_account)
            time.sleep(2)
            
            #Angegebener Account wird geklickt
            account_link = self.wait.until(EC.element_to_be_clickable(
                (By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div[2]/div/div/div/div[2]/div/div/div[3]/div/a[1]")))
            account_link.click()
            print(f"Navigated to {self.target_account}'s profile")
            time.sleep(5)
            
        except Exception as e:
            print(f"Navigation to target account failed: {str(e)}")
            self.quit()

    def interact_with_posts(self, num_posts=1):
        try:
            # Click on first post
            first_post = self.wait.until(EC.element_to_be_clickable(
                (By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[2]/div/div[1]/section/main/div/div[2]/div/div/div/div[1]/div[1]/a")))
            first_post.click()
            time.sleep(3)
            
            for _ in range(num_posts):
                #Beitrag liken
                like_btn = self.wait.until(EC.element_to_be_clickable(
                    (By.XPATH, "/html/body/div[5]/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[1]/span[1]/div/div")))
                like_btn.click()
                print("Beitrag geliket")
                time.sleep(random.uniform(1, 3))
                
                #Beitrag speichern
                save_btn = self.driver.find_element(By.XPATH,
                    "/html/body/div[5]/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[1]/span[4]/div/div")
                save_btn.click()
                print("Beitrag gespeichert")
                time.sleep(random.uniform(1, 3))
                
                #Nächster Beitrag
                next_btn = self.driver.find_element(By.XPATH,
                    "/html/body/div[5]/div[1]/div/div[3]/div/div/div/div/div[1]/div/div/div/button")
                next_btn.click()
                print("Nächster Beitrag")
                time.sleep(random.uniform(2, 5))
                
        except Exception as e:
            print(f"Post interaction failed: {str(e)}")
            self.quit()

    def quit(self):
        print("Browser schlie0en")
        self.driver.quit()

    def run(self):
        try:
            self.login()
            self.navigate_to_target_account()
            self.interact_with_posts(num_posts=3)
            
            # Add some random delay before closing
            time.sleep(random.uniform(2, 5))
            
        except Exception as e:
            print(f"Error occurred: {str(e)}")
        finally:
            self.quit()

if __name__ == "__main__":
    bot = InstagramBot()
    bot.run()
