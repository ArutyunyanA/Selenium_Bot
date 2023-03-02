# importing necessary libraries

from selenium.webdriver.common.by import  By
from selenium.webdriver.remote.webelement import WebElement

# building get_data class to collect all results

class GetData:
    
    def __init__(self, data_box:WebElement):
        self.data_box = data_box
        self.deal_box = self.pull_data_box()

# function to find needed to us container with data

    def pull_data_box(self):
        return self.data_box.find_elements(
            By.CLASS_NAME, 'Search__result-container' # here you sgould specify your CSS selectors
        )

# Collectiong data from inside the container box with spicification of needed CSS selectors or 

    def pull_titles(self):
        collection = []
        for data in self.deal_box:
            doc_names = data.find_element(
                By.CLASS_NAME, 'Search__result-name'
            ).text.title().strip()
            doc_spec = data.find_element(
                By.CLASS_NAME, 'Search__result-speciality'
            ).text.title().strip()
            doc_address = data.find_element(
                By.CLASS_NAME, 'dsg-no-mg-bottom'
            ).get_attribute('innerHTML').title().strip()
            collection.append(
                [doc_names, doc_spec, doc_address]
            )

        return collection



