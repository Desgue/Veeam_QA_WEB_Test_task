from selenium import webdriver
from selenium.webdriver.chrome.service import  Service
from selenium.webdriver.common.by import  By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def New_Driver():
    service = Service(executable_path =  'chromedriver.exe')
    driver = webdriver.Chrome(service = service)
    driver.get('https://careers.veeam.com/vacancies ')
    driver.maximize_window()
    return driver

def Get_Department_Toggler(driver):
    toggler = driver.find_element(By.ID, 'department-toggler')
    return toggler


# City and country toggler have both the same ID of 'city-toggler'
def Get_Country_Toggler(driver):
    toggler = driver.find_element(By.XPATH, '//*[@id="city-toggler"]')
    return toggler


def Select_Department(driver, department_name):
    department_toggler = Get_Department_Toggler(driver)
    department_toggler.click()
    department = driver.find_element(By.XPATH, "//div[@class='scrollarea-content content']/a[contains(text(), '{}')]".format(department_name))
    department.click()
    return



if __name__ == '__main__':
    driver = New_Driver()
    Select_Department(driver, "Sales")

    


    driver.quit()
    pass