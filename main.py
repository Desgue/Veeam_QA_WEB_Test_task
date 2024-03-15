""" from selenium import webdriver
from selenium.webdriver.chrome.service import  Service
from selenium.webdriver.common.by import  By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

COUNTRY_TOGGLER_IDX = 0
CITY_TOGGLER_IDX = 1
DEPARTMENT_SCROLLAREA_IDX = 0
COUNTRY_SCROLLAREA_IDX = 1
CITY_SCROLLAREA_IDX = 2

USA_STATE_TOGGLER_IDX = 1
USA_CITY_TOGGLER_IDX = 2
USA_STATE_SCROLLAREA_IDX = 2
USA_CITY_SCROLLAREA_IDC = 3


def New_Driver():
    service = Service(executable_path =  'chromedriver.exe')
    driver = webdriver.Chrome(service = service)
    driver.get('https://careers.veeam.com/vacancies ')
    driver.maximize_window()
    driver.implicitly_wait(2)
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
    area = Get_Scroll_Area(driver)[DEPARTMENT_SCROLLAREA_IDX]

    for i in range(10):
        driver.execute_script("arguments[0].scrollBy(0,50);", area) 
        try:    
            department = driver.find_element(By.LINK_TEXT, department_name)
            department.click()
            break
        except Exception as e:
            continue


# City, country and State toggler have all the same ID of 'city-toggler'
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
    country_toggler = Get_City_Togglers(driver)[COUNTRY_TOGGLER_IDX]
    country_toggler.click()


    area = Get_Scroll_Area(driver)[COUNTRY_SCROLLAREA_IDX]
    for i in range(10):
        driver.execute_script("arguments[0].scrollBy(0,200);", area) 
        try:    
            department = driver.find_element(By.LINK_TEXT, country_name)
            department.click()
            break
        except Exception as e:
            continue


# SELECT STATE IF COUNTRY IS USA
def Select_State(driver, state_name):
    state_toggler = Get_City_Togglers(driver)[USA_STATE_TOGGLER_IDX]
    state_toggler.click()

    area = Get_Scroll_Area(driver)

    for i in range(10):
        driver.execute_script("arguments[0].scrollBy(0,200);", area[2]) 
        try:    
            state = driver.find_element(By.LINK_TEXT, state_name)
            state.click()
            break
        except Exception as e:
            continue


# SELECT CITY

def Select_City(driver, city_name, is_usa = False):
    if is_usa:
        city_idx = USA_CITY_TOGGLER_IDX
        area_idx = USA_CITY_SCROLLAREA_IDC
    else:
        city_idx = CITY_TOGGLER_IDX
        area_idx = CITY_SCROLLAREA_IDX

    city_toggler = Get_City_Togglers(driver)[city_idx]
    city_toggler.click()

    area = Get_Scroll_Area(driver)

    for i in range(10):
        driver.execute_script("arguments[0].scrollBy(0,200);", area[area_idx]) 
        try:    
            department = driver.find_element(By.LINK_TEXT, city_name)
            department.click()
            break
        except Exception as e:
            continue    

# CLICK SEARCH BUTTON
def Click_Search_Button(driver):
    search_button = driver.find_element(By.XPATH, "//button[text()='Find a career']")
    search_button.click()
    return


# SCROLL MAIN BODY
def Scroll_Main_Body(driver):
    body = driver.find_element(By.TAG_NAME, 'html')

    for i in range(60):
        driver.execute_script("arguments[0].scrollBy(0,100);", body)
        
    return

# 4 HIDDEN JOB CARDS FOR EACH JOB FOUND IN THE SEARCH
# 3 CARDS ARE DISPLAYED DEPENDING ON THE SIZE OF THE SCREEN
# 1 CARD IS APPARENTLY HIDDEN ALWAYS
# REQUIREMENT IS TO MAXIMAZE THE SCREEN SO FOCUS ON THAT DISPLAYED CARD
def Collect_Job_Information(driver):
    job_list = driver.find_elements(By.XPATH, '//div[@class="row d-none d-md-block"]/div/div/div[@class="d-none d-lg-block"]/a[@class="card card-md-45 card-no-hover card--shadowed"]')
    return

if __name__ == '__main__':
    department = "Sales"
    country = "Romania"
    city = "Bucharest"
    state = "Texas"

    driver = New_Driver()
    Select_Department(driver, department)
    Select_Country(driver, country)
    if country == "USA":
        Select_State(driver, state)
        Select_City(driver, city, True)
    else: 
        Select_City(driver, city)
    
    Click_Search_Button(driver)
    Collect_Job_Information(driver)

    driver.quit()
    pass

# GAME PLAN
# 1. Get the department toggler - DONE
# 2. Click the department toggler - DONE
# 3. Check if the department is visible - DONE
# 4. If the department is visible, click the department - DONE
# 5. If the department is not visible, scroll to the department and click the department - DONE
# 6. Get the country toggler - DONE
# 7. Check if the country is visible - DONE
# 8. If the country is USA, I have to click the State toggler and select the state before the city - DONE
# 9. If the country is not USA, I only have to click the city toggler - DONE
# 10. Check if the city is visible - DONE
# 11. If the city is visible, click the city - DONE
# 12. If the city is not visible, scroll to the city and click the city - DONE
# 13. Click the search button

# TO DO
# 1. CHANGE SCROLLAREA SELECTION TO A MORE SPECIFIC SELECTOR
# 2. REFACTOR THE CODE TO MAKE IT MORE READABLE
# 3. ADD EXCEPTION HANDLING
# 4. ADD LOGGING
# 5. TRANSFORM IN CLI TOOL """

import scraper

if __name__ == '__main__':
    tester1 = scraper.Tester(
                            url="https://careers.veeam.com/vacancies",
                            department="Sales",
                            country="USA",
                            state="Texas",
                            city="Austin",
                            num_jobs_to_compare=1)
    tester2 = scraper.Tester(
                            url="https://careers.veeam.com/vacancies",
                            department="Sales",
                            country="Romania",
                            city="Bucharest",
                            num_jobs_to_compare=28)  

    tester1.run()
    tester2.run()