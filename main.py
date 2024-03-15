from selenium import webdriver
from selenium.webdriver.chrome.service import  Service
from selenium.webdriver.common.by import  By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time


def New_Driver():
    service = Service(executable_path =  'chromedriver.exe')
    driver = webdriver.Chrome(service = service)
    driver.get('https://careers.veeam.com/vacancies ')
    driver.maximize_window()
    
    return driver

# GET SCROLLABLE AREA AFTER CLICKING A TOGGLER
# 0 = Department, 1 = Country, IF COUNTRY USA 2 = STATE 3 = CITY, IF COUNTRY IS NOT USA, 2 = CITY
def Get_Scroll_Area(driver):
    scroll_area = driver.find_elements(By.XPATH, '//*[@class="scrollarea area"]')
    return scroll_area

# HANDLE DEPARTMENT SELECTION

def Click_Department_Toggler(driver):
    toggler = driver.find_element(By.ID, 'department-toggler')
    toggler.click()
    return

def Select_Department(driver, department_name):
    Click_Department_Toggler(driver)
    area = Get_Scroll_Area(driver)[0]

    for i in range(10):
        driver.execute_script("arguments[0].scrollBy(0,50);", area) 
        try:    
            department = driver.find_element(By.LINK_TEXT, department_name)
            department.click()
            break
        except Exception as e:
            continue


# City and country toggler have both the same ID of 'city-toggler'
def Get_City_Togglers(driver):
    # 0 = Country, 1 = City or State 2 = City if State is selected
    toggler = driver.find_elements(By.XPATH, '//*[@id="city-toggler"]')
    return toggler

# Some countries work, some countries throw error "Element not interactable" Countries valid up to "Costa Rica"
# Problem might be visinilty of the element as we are dealing not with a select element but with a div element
# FIX DEPARTMENT SELECTION WHEN FINDING A SOLUTION FOR COUNTRY SELECTION
# ELEMENTS ARE ONLY VISIBLE UNTIL COSTA RICA CONFIRMING ASSUMPTION OF VISIBILITY


def Select_Country(driver, country_name):
    country_toggler = Get_City_Togglers(driver)[0]
    country_toggler.click()


    area = Get_Scroll_Area(driver)[1]
    for i in range(10):
        driver.execute_script("arguments[0].scrollBy(0,100);", area) 
        try:    
            department = driver.find_element(By.LINK_TEXT, country_name)
            department.click()
            break
        except Exception as e:
            continue
    
    

    """ country = driver.find_element(By.LINK_TEXT, country_name)
    actions = ActionChains(driver)
    actions.move_to_element(country).perform()
    country.click() """
    
        
if __name__ == '__main__':
    department = "Sales"
    country = "Romania"

    driver = New_Driver()
    
    Select_Department(driver, department)
    Select_Country(driver, country)

    time.sleep(5)
    


    driver.quit()
    pass

# GAME PLAN
# 1. Get the department toggler - DONE
# 2. Click the department toggler - DONE
# 3. Check if the department is visible
# 4. If the department is visible, click the department
# 5. If the department is not visible, scroll to the department and click the department
# 6. Get the country toggler
# 7. Check if the country is visible
# 8. If the country is USA, I have to click the State toggler and select the state before the city
# 9. If the country is not USA, I only have to click the city toggler
# 10. Check if the city is visible
# 11. If the city is visible, click the city
# 12. If the city is not visible, scroll to the city and click the city
# 13. Click the search button

# TO DO
# 1. CHANGE SCROLLAREA SELECTION TO A MORE SPECIFIC SELECTOR
