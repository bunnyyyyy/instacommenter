import os
import time
import sys
import random
import spintax
import requests
import numpy as np
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from sanyacreds import username as usr, password as passw
from webdriver_manager.firefox import GeckoDriverManager as GM
from selenium.webdriver.firefox.options import Options


sys.setrecursionlimit(10**6)

with open(r'comments.txt', 'r') as f:
    commentsl = [line.strip() for line in f]

class Bot:
    def __init__(self, username, password):
        options = Options()
        options.headless = True
        self.count = 0
        self.success = 0
        self.block = 0
        self.link = 'https://www.instagram.com/p/CufvbjBv6JT/'
        self.username = username
        self.password = password
        user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/109.0"
        profile = webdriver.FirefoxProfile()
        profile.set_preference("general.useragent.override", user_agent)
        self.bot = webdriver.Firefox(profile, executable_path=GM().install())
        #self.bot.set_window_size(1600, 800)
       

    def exit(self):
        bot = self.bot
        bot.quit()

    def login(self):
        bot = self.bot
        bot.get('https://instagram.com/')
        
        # bot.find_element_by_xpath('/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/article/div/div/div/div/div[2]/div[3]/button[1]').click()
        time.sleep(5)

        if check_exists_by_xpath(bot, "//button[text()='Accept']"):
            print("No cookies")
        else:
            bot.find_element_by_xpath("//button[text()='Accept']").click()
            print("Accepted cookies")

        
        print("Logging in...")
        time.sleep(1)
        username_field = bot.find_element_by_xpath(
            '/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input')
        username_field.send_keys(self.username)

        find_pass_field = (
            By.XPATH, '/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input')
        WebDriverWait(bot, 25).until(
            EC.presence_of_element_located(find_pass_field))
        pass_field = bot.find_element(*find_pass_field)
        WebDriverWait(bot, 25).until(
            EC.element_to_be_clickable(find_pass_field))
        pass_field.send_keys(self.password)
        bot.find_element_by_xpath(
            '/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]/button').click()
        time.sleep(6)

    def get_posts(self):
        print('Searching for post...')
        link = self.link
        self.bot.get(link)
        time.sleep(1)
       
        return run.comment(random_comment())


    def comment(self, comment):

        bot = self.bot

        
       
       
        

        find_comment_box = (
            By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div[1]/div/div[2]/div/section/div/form/div/textarea')
        WebDriverWait(self.bot, 25).until(
            EC.presence_of_element_located(find_comment_box))
        comment_box = self.bot.find_element(*find_comment_box)
        WebDriverWait(self.bot, 25).until(
            EC.element_to_be_clickable(find_comment_box))
        # comment_box.click()
        self.count = self.count + 1
        print(f"Entering...{self.count}")
        comment_box.send_keys(comment)
        time.sleep(1)

        find_post_button = (
            By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div[1]/div/div[2]/div/section/div/form/div/div[2]/div')
        WebDriverWait(self.bot, 25).until(
            EC.presence_of_element_located(find_post_button))
        post_button = self.bot.find_element(*find_post_button)

        
        WebDriverWait(self.bot, 10).until(
            EC.element_to_be_clickable(find_post_button))
        
       
        if check_exists_by_xpath(bot, "//button[text()='OK']"):
            post_button.click()

            time.sleep(3)

            if check_exists_by_xpath(bot, "//button[text()='OK']"):
                self.success = self.success + 1
                print(f"Successful...{self.success}")
        else:
            bot.find_element_by_xpath("//button[text()='OK']").click()
            self.block = self.block + 1
            comment_box.clear()
            print(f"Blocked...{self.block}")
            print(f"Successful (not this time)...{self.success}")
            time.sleep(300)


        
       
        time.sleep(random.randint(1, 3))
        return run.comment(random_comment())


def random_comment():
    
    comment = random.choice(commentsl)
    return comment


def check_exists_by_xpath(driver, xpath):
    try:
        driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return True

    return False


run = Bot(usr, passw)
run.login()

if __name__ == '__main__':
    run.get_posts()
