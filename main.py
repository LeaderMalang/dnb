# This is a sample Python script.
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
driver = webdriver.Firefox()

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.



    driver.get('https://www.dnb.com/business-directory/company-information.agriculture-forestry-sector.bg.html?page=1') # Press Ctrl+F8 to toggle the breakpoint.
    page_tile=driver.title
    wait = WebDriverWait(driver, 50)
    if page_tile=='Find Agriculture & Forestry Companies in Bulgaria - Dun & Bradstreet':
        print(page_tile)
        address_table = wait.until(
            EC.presence_of_element_located((By.ID, "companyResults"))

        )
        companies_elements = driver.find_elements(By.CLASS_NAME, 'data')
        for company in companies_elements:
            print(company.text)

        while True:

            next_page_element = driver.find_element(By.CLASS_NAME, 'next')
            next_a_element=next_page_element.find_element(By.XPATH,'//a')
            next_a_element.click()
            print("Processing page")

            try:
                address_table = wait.until(
                    EC.presence_of_element_located((By.ID, "companyResults"))

                )
                companies_elements = driver.find_elements(By.CLASS_NAME, 'data')
                for company in companies_elements:
                    print(company.text)

            except NoSuchElementException:
                print("Exiting. Last page")
                break

            # TODO: save the page



    driver.close()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
