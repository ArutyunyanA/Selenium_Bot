

import os
import time
from selenium.webdriver.common.by import By
import Monitoring.Constatn as Const
from selenium.webdriver.common.keys import Keys
from Monitoring.Report import GetData
from selenium import webdriver
from prettytable import PrettyTable



class Monitoring(webdriver.Chrome):
    
    def __init__(self, driver_path = '/Users/macintosh/python/Selenium_Bot/webdriver', teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += self.driver_path
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        super(Monitoring, self).__init__(options=options)
        self.implicitly_wait(20)
        self.maximize_window()


    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def land_first_page(self):
        self.get(Const.BASE_URL)


    def choose_qualification(self):
        chose = self.find_element(
            By.CSS_SELECTOR, 'input[placeholder="Specialty & expertise"]'
        )
        chose.click()
        chose.send_keys('Endodontist')
        chose.send_keys(Keys.ENTER)
        chose.click()
        button_find = self.find_element(By.ID, 'submitSearch')
        button_find.click()


    def scroll(self):
        time.sleep(5)
        self.execute_script("window.scrollTo(0,document.body.scrollHeight)")


    def push_the_button(self):
            while True:
                try:
                    btn = self.find_element(By.CLASS_NAME, 'dsg-align')
                    btn.click()
                except Exception:
                        break


    def results(self):
        doc_data = self.find_element(
            By.ID, 'doctor-listing-container'
        )
        report = GetData(doc_data)
        table = PrettyTable(
            ['Doctor Names', 'Speciality', 'Address']
        )
        table.add_rows(report.pull_titles())
        print(table)


