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
# 0 = Department, 1 = Country,  2 = STATE(IF COUNTRY USA) OR CITY  3 = CITY (ONLY IF COUNTRY USA)
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
        driver.implicitly_wait(2)


# City and country toggler have both the same ID of 'city-toggler'
def Get_City_Togglers(driver):
    # 0 = Country, 1 = City or State,  2 = City if State is selected
    toggler = driver.find_elements(By.XPATH, '//*[@id="city-toggler"]')
    return toggler

# Some countries work, some countries throw error "Element not interactable" Countries valid up to "Costa Rica"
# Problem might be visinilty of the element as we are dealing not with a select element but with a div element
# FIX DEPARTMENT SELECTION WHEN FINDING A SOLUTION FOR COUNTRY SELECTION
# ELEMENTS ARE ONLY VISIBLE UNTIL COSTA RICA CONFIRMING ASSUMPTION OF VISIBILITY


# SELECT COUNTRY

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
        driver.implicitly_wait(2)


# SELECT STATE IF COUNTRY IS USA
def Select_State(driver, state_name):
    state_toggler = Get_City_Togglers(driver)[1]
    state_toggler.click()

    area = Get_Scroll_Area(driver)
    print(len(area))
    for i in range(10):
        driver.execute_script("arguments[0].scrollBy(0,100);", area[2]) 
        try:    
            state = driver.find_element(By.LINK_TEXT, state_name)
            state.click()
            break
        except Exception as e:
            continue


# SELECT CITY

def Select_City(driver, city_name, is_usa = False):
    if is_usa:
        city_idx = 2
        area_idx = 3
    else:
        city_idx = 1
        area_idx = 2

    city_toggler = Get_City_Togglers(driver)[city_idx]
    city_toggler.click()

    area = Get_Scroll_Area(driver)
    for a in area:
        print(a.tag_name)
    for i in range(10):
        driver.execute_script("arguments[0].scrollBy(0,100);", area[area_idx]) 
        try:    
            department = driver.find_element(By.LINK_TEXT, city_name)
            department.click()
            break
        except Exception as e:
            continue    

        
if __name__ == '__main__':
    department = "Sales"
    country = "USA"
    city = "Austin"
    state = "Texas"

    driver = New_Driver()

    Select_Department(driver, department)
    Select_Country(driver, country)
    if country == "USA":
        Select_State(driver, state)
        Select_City(driver, city, True)
    else: 
        Select_City(driver, city)
    
    time.sleep(10)
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
