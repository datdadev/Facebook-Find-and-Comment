from http.cookies import Morsel
import sys
from tabnanny import check
from selenium import webdriver as wdr
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
import os
import json
import pickle
import re
import pyperclip
import html2text
from time import sleep

class Facebook:
    def __init__(self, **kwargs):
        self.facebook_login = kwargs['facebook_login']
        self.facebook_password = kwargs['facebook_password']
        self.refresh_time = kwargs['refresh_time']
        
        options = wdr.EdgeOptions()
        options.binary_location = r"/usr/bin/microsoft-edge-stable"
        options.set_capability("platform", "LINUX")
        self.wdr = wdr.Edge(executable_path=r"./msedgedriver", options=options)
        
        self.wdr.get("https://mbasic.facebook.com/")
        
    def login_facebook(self):
        if os.path.getsize("./my_cookies.pkl") == 0:
            self.wdr.find_element(By.XPATH, '//input[@name="email"]').send_keys(self.facebook_login)
            self.wdr.find_element(By.XPATH, '//input[@name="pass"]').send_keys(self.facebook_password)
            self.wdr.find_element(By.XPATH, '//input[@name="login"]').click()
            sleep(5)
            pickle.dump(self.wdr.get_cookies(), open("my_cookies.pkl", "wb"))
            print("Saved Cookies!")
        else:
            cookies = pickle.load(open("my_cookies.pkl", "rb"))
            for cookie in cookies:
                self.wdr.add_cookie(cookie)
            self.wdr.get("https://mbasic.facebook.com/")
    
    def close_save_device_page(self):
            if 'save-device' in self.wdr.current_url:
                  self.wdr.find_element(By.XPATH, '//a').click()
    
    def current_url_to_text(self):
        try:
            sleep(1)
            myElem = WebDriverWait(self.wdr, 2).until(EC.presence_of_element_located((By.NAME, 'query')))
            html = self.wdr.find_element_by_xpath("//html").get_attribute('outerHTML')
            with open('./textFiles/file.txt', 'wb') as out:
                out.write(html2text.html2text(str(html)).encode('utf-8'))
            #print("Page loaded!")
        except TimeoutException:
            print("Loading took too much time! Check your account!")
            sys.exit()
    
    def check_and_save_commentedPosts(self, regex_texts, urls):
        definedUrls = []
        matched_indexUrl = []
        if os.path.getsize('commentedPosts.json') != 0:
            with open('commentedPosts.json', 'r') as f:
                definedUrls = json.load(f)
            for indexUrl, url in enumerate(urls):
                textFound = False
                for i in range(0, len(definedUrls)):
                    if (url == definedUrls[i]["Url"]):
                        textFound = True
                        matched_indexUrl.append(indexUrl)
                        break
                if textFound == False:
                    definedUrls.append({"Text": regex_texts[indexUrl], "Url": url})
            for i in range(len(matched_indexUrl)-1, -1, -1):
                urls.remove(urls[matched_indexUrl[i]])
        else:
            for i in range(len(urls)):
                definedUrls.append({"Text": regex_texts[i], "Url": urls[i]})
        json_object = json.dumps(definedUrls, indent=4)
        with open('commentedPosts.json', 'w') as f:
            f.write(json_object)
        return urls
    
    def comment(self):
        text_found = False
        regex_texts = []
        urls = []
        with open('./textFiles/regex_find.txt', 'r') as str:
            text_to_find = str.read()
        with open('./textFiles/file.txt', 'r') as file:
            for line in file.readlines():
                if text_found == False:
                    if re.search(text_to_find, line):
                        text = re.search(text_to_find, line).group()
                        regex_texts.append(text)
                        text_found = True
                else:
                    if re.search("Comment(s)?\]\(+(.)+\)", line):
                        comment_finder = re.search("Comment(s)?\]\(+(.)+\)", line).group()
                        cmt_url = re.sub("Comment(s)?]\(", "", comment_finder.strip(")"))
                        urls.append(cmt_url)
                        text_found = False
        if urls: #List is not empty!
            filteredUrls = self.check_and_save_commentedPosts(regex_texts, urls)
            if filteredUrls: #FilteredList is not empty!
                for url in filteredUrls:
                    self.wdr.get(url)
                    self.comment_click()
    
    def comment_click(self):
        with open('./textFiles/comment.txt', 'r') as post_file:
            all_lines = post_file.readlines()
            post = ''.join([str(line) for line in all_lines])
            post_box = self.wdr.find_element(By.XPATH, "//input[@name='comment_text']")
            pyperclip.copy(post)
            act = ActionChains(self.wdr)
            act.click(on_element = post_box)
            act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
            self.wdr.find_element(By.XPATH, "//input[@value='Comment']").click()
            print("Commented!")
    
    def get_stories(self):
        try:
            with open('./textFiles/file.txt', 'r') as file:
                str = file.read()
                next_posts = r"https://mbasic.facebook.com"+re.findall("\/stories+.+\)", str)[0].strip(")")
                return next_posts
        except:
            print("No more post!")
            self.wdr.quit()
            sys.exit()
    
    def looping(self):
        for i in range(-1, self.refresh_time):
            print("Attempt {0}".format(i+1))
            self.current_url_to_text()
            try:
                self.comment()
            except:
                pass
            self.wdr.get(self.get_stories())
        print("Finished!")
    
    def run(self):
        self.login_facebook()
        self.close_save_device_page()
        self.looping()
        
        self.wdr.quit()
        
    