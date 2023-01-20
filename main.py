import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random

PROMISED_DOWN = 100
PROMISED_UP = 20
TWITTER_EMAIL = os.environ.get("TWITTER_EMAIL")
TWITTER_PASSWORD = os.environ.get("TWITTER_PASSWORD")


class InternetSpeedTwitterBot:

    def __init__(self):
        geo_location = webdriver.FirefoxOptions()
        geo_location.set_preference('geo.prompt.testing', True)
        geo_location.set_preference('geo.prompt.testing.allow', True)
        self.driver = webdriver.Firefox(options=geo_location)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get('https://www.speedtest.net/')
        time.sleep(2)
        go_button = self.driver.find_element(By.CSS_SELECTOR, '.start-text')
        go_button.click()
        time.sleep(40)
        self.down = float(self.driver.find_element(By.CSS_SELECTOR, '.download-speed').text)
        self.up = float(self.driver.find_element(By.CSS_SELECTOR, '.upload-speed').text)

    def tweet_at_provider(self):
        if self.down < PROMISED_DOWN:
            self.driver.get('https://twitter.com/login')
            time.sleep(3)
            email = self.driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div['
                                                       '2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div['
                                                       '2]/div/input')
            email.send_keys(TWITTER_EMAIL)
            time.sleep(random.randint(3, 5))
            # click on next
            next_button = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div['
                                                             '1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div['
                                                             '2]/div[2]/div/div/div/div[6]/div')
            next_button.click()
            time.sleep(random.randint(1, 3))
            password = self.driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div['
                                                          '2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div['
                                                          '3]/div/label/div/div[2]/div[1]/input')
            password.send_keys(TWITTER_PASSWORD)
            time.sleep(random.randint(1, 3))
            # click on login
            login_button = self.driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div['
                                                              '2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div['
                                                              '1]/div/div/div/div')
            login_button.click()
            time.sleep(random.randint(1, 3))
            tweet_button = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/header/div/div/div/div['
                                                              '1]/div[3]/a/div')
            tweet_button.click()
            time.sleep(random.randint(1, 3))
            tweet_composer = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/div['
                                                                '2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div['
                                                                '3]/div[2]/div[1]/div/div/div/div/div[2]/div['
                                                                '1]/div/div/div/div/div/div[2]/div/div/div/div/label/div['
                                                                '1]/div/div/div/div/div/div[2]/div')
            message = f"Test tweet for DAY51 of #100DaysOfPython Twitter bot: Hey Internet Provider! " \
                      f"Why is my internet speed {self.down} down/{self.up} up when I pay " \
                      f"for {PROMISED_DOWN} down/{PROMISED_UP} up?"
            tweet_composer.send_keys(message)
            time.sleep(2)
            send_tweet = self.driver.find_element(By.XPATH, '//*[text()="Tweet"]')
            send_tweet.click()


internet_speed = InternetSpeedTwitterBot()
internet_speed.get_internet_speed()
internet_speed.tweet_at_provider()
