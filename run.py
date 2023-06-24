import os
import time
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
from credentials import username as usr, password as passw
from webdriver_manager.firefox import GeckoDriverManager as GM



class Bot:
    def __init__(self, username, password):
        self.link = 'https://www.instagram.com/p/B_S6lA1gyVs/'
        self.username = username
        self.password = password
        user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/109.0"
        profile = webdriver.FirefoxProfile()
        profile.set_preference("general.useragent.override", user_agent)
        self.bot = webdriver.Firefox(profile, executable_path=GM().install())
        self.bot.set_window_size(1600, 800)
        with open(r'tags.txt', 'r') as f:
            tagsl = [line.strip() for line in f]
        self.tags = tagsl
        self.urls = []

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
            '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input')
        username_field.send_keys(self.username)

        find_pass_field = (
            By.XPATH, '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input')
        WebDriverWait(bot, 25).until(
            EC.presence_of_element_located(find_pass_field))
        pass_field = bot.find_element(*find_pass_field)
        WebDriverWait(bot, 25).until(
            EC.element_to_be_clickable(find_pass_field))
        pass_field.send_keys(self.password)
        bot.find_element_by_xpath(
            '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]/button').click()
        time.sleep(4)

    def get_posts(self):
        print('Searching for post...')
        bot = self.bot
        link = self.link
        bot.get(link)
        return run.comment(random_comment())


    def comment(self, comment):

        bot = self.bot
        url = self.link
        print('commenting...')
        bot.get(url)
        bot.implicitly_wait(1)

        # bot.execute_script("window.scrollTo(0, window.scrollY + 300)")
        time.sleep(2)

        # bot.find_element_by_xpath(
        #     '/html/body/div[1]/section/main/div/div/article/div[3]/section[1]/span[1]/button').click()
        # time.sleep(2)

        # bot.find_element_by_xpath(
        #     '//*[@id="react-root"]/section/main/div/div[1]/article/div[3]/section[1]/span[2]/button').click()

        

        find_comment_box = (
            By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div[1]/div/div[2]/div/section/div/form/div/textarea')
        WebDriverWait(bot, 25).until(
            EC.presence_of_element_located(find_comment_box))
        comment_box = bot.find_element(*find_comment_box)
        WebDriverWait(bot, 25).until(
            EC.element_to_be_clickable(find_comment_box))
        # comment_box.click()
        print("Entering...")
        time.sleep(2)
        comment_box.send_keys(comment)

        find_post_button = (
            By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div[1]/div/div[2]/div/section/div/form/div/div[2]/div')
        WebDriverWait(bot, 25).until(
            EC.presence_of_element_located(find_post_button))
        post_button = bot.find_element(*find_post_button)
        WebDriverWait(bot, 25).until(
            EC.element_to_be_clickable(find_post_button))
        post_button.click()

        # edit this line to make bot faster
        time.sleep(7)


        return run.comment(random_comment())


def random_comment():
    with open(r'comments.txt', 'r') as f:
        commentsl = [line.strip() for line in f]
    comments = commentsl
    comment = random.choice(comments)
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
