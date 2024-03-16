from selenium import webdriver
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
USA_CITY_SCROLLAREA_IDX = 3

class Options:
    def __init__(self, url, department, country, city, num_jobs_to_compare, state=None, driver_path = "chromedriver.exe"):
        self.url = url
        self.department = department
        self.country = country
        self.city = city
        self.state = state
        self.num_jobs_to_compare = num_jobs_to_compare
        self.driver_path = driver_path

class Tester:
    def __init__(self, options: Options):
        self.url = options.url
        self.department = options.department
        self.country = options.country
        self.city = options.city
        self.state = options.state
        self.num_jobs_to_compare = options.num_jobs_to_compare
        self.init_Driver(options.driver_path)

    def init_Driver(self, driver_path):
        service = Service(executable_path = driver_path)
        self.driver = webdriver.Chrome(service = service)
        
        pass

    def open_browser(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        
        pass

    def close_browser(self):
        self.driver.quit()
        pass
    
    def get_city_togglers(self):
        return  self.driver.find_elements(By.XPATH, '//*[@id="city-toggler"]')
        

    def get_scroll_area(self):
        return  self.driver.find_elements(By.XPATH, '//*[@class="scrollarea area"]')
    
    def click_Department_Toggler(self):
        toggler = self.driver.find_element(By.ID, 'department-toggler')
        toggler.click()
        return


    def select_Department(self):
        self.click_Department_Toggler()
        area = self.get_scroll_area()[DEPARTMENT_SCROLLAREA_IDX]

        for i in range(10):
            self.driver.execute_script("arguments[0].scrollBy(0,50);", area) 
            try:    
                department = self.driver.find_element(By.LINK_TEXT, self.department)
                department.click()
                break
            except Exception as e:
                continue
    

    def select_country(self):
        toggler = self.get_city_togglers()[COUNTRY_TOGGLER_IDX]
        toggler.click()

        area = self.get_scroll_area()[COUNTRY_SCROLLAREA_IDX]
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollBy(0,200);", area) 
            try:    
                country = self.driver.find_element(By.LINK_TEXT, self.country)
                country.click()
                break
            except Exception as e:
                continue    
         

    def select_state(self):
        toggler = self.get_city_togglers()[USA_STATE_TOGGLER_IDX]
        toggler.click()

        area = self.get_scroll_area()[USA_STATE_SCROLLAREA_IDX]

        for i in range(10):
            self.driver.execute_script("arguments[0].scrollBy(0,200);", area) 
            try:    
                state_option = self.driver.find_element(By.LINK_TEXT, self.state)
                state_option.click()
                break
            except Exception as e:
                continue 
        

    def select_city_with_state(self):
        self.get_city_togglers()[USA_CITY_TOGGLER_IDX].click()

        area = self.get_scroll_area()[USA_CITY_SCROLLAREA_IDX]
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollBy(0,100);", area) 
            try:    
                department = self.driver.find_element(By.LINK_TEXT, self.city)
                department.click()
                break
            except Exception as e:
                continue          
        pass

    def select_city_without_state(self):
        self.get_city_togglers()[CITY_TOGGLER_IDX].click()

        area = self.get_scroll_area()[CITY_SCROLLAREA_IDX]
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollBy(0,200);", area) 
            try:    
                department = self.driver.find_element(By.LINK_TEXT, self.city)
                department.click()
                break
            except Exception as e:
                continue          
        pass

    def click_search_button(self):
        self.driver.find_element(By.XPATH, "//button[text()='Find a career']").click()
        pass
    
    def set_available_jobs_list(self):
        self.job_list = self.driver.find_elements(By.XPATH, '//div[@class="row d-none d-md-block"]/div/div/div[@class="d-none d-lg-block"]/a[@class="card card-md-45 card-no-hover card--shadowed"]')
        
    
    def scrape(self):
        self.open_browser()
        self.select_Department()
        self.select_country()
        if self.state:
            self.select_state()
            self.select_city_with_state()

        else:
            self.select_city_without_state()

        self.click_search_button()
        
        self.set_available_jobs_list()

    def jobs_found_match_expected(self):
        return len(self.job_list) == self.num_jobs_to_compare
    
    def run(self):
        self.scrape()
        if self.jobs_found_match_expected():
            print("Test Passed, the number of jobs displayed is as expected")
            print("Number of jobs displayed: ", len(self.job_list))
            print("Number of jobs expected: ", self.num_jobs_to_compare)
        else:
            print("Test Failed, the number of jobs displayed is not as expected")
            print("Number of jobs displayed: ", len(self.job_list))
            print("Number of jobs expected: ", self.num_jobs_to_compare)
        self.close_browser()
