from selenium import webdriver
from selenium.webdriver.chrome.service import  Service
from selenium.webdriver.common.by import  By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time


DEPARTMENT_SCROLLAREA_IDX = 0
COUNTRY_SCROLLAREA_IDX = 1
WITHOUT_STATE_CITY_SCROLLAREA_IDX = 2
STATE_SCROLLAREA_IDX = 2
WITH_STATE_CITY_SCROLLAREA_IDX = 3

COUNTRY_TOGGLER_IDX = 0
WITHOUT_STATE_CITY_TOGGLER_IDX = 1
STATE_TOGGLER_IDX = 1
WITH_STATE_CITY_TOGGLER_IDX = 2

TOGGLER_ID_XPATH_SELECTOR = '//*[@id="city-toggler"]'
SCROLL_AREA_XPATH_SELECTOR = '//*[@class="scrollarea area"]'
DEPATRMENT_TOGGLER_CSS_ID = 'department-toggler'
SEARCH_BUTTON_XPATH_SELECTOR = "//button[text()='Find a career']"
JOB_CARD_XPATH_SELECTOR = '//div[@class="row d-none d-md-block"]/div/div/div[@class="d-none d-lg-block"]/a[@class="card card-md-45 card-no-hover card--shadowed"]'

class Options:
    def __init__(
        self, 
        url, 
        department, 
        country, 
        city, 
        num_jobs_to_compare, 
        state=None, 
        driver_path = "chromedriver.exe"):
        
        """ Options Class that defines the test parameters """
        self.url = url
        self.department = department
        self.country = country
        self.city = city
        self.state = state
        self.num_jobs_to_compare = num_jobs_to_compare
        self.driver_path = driver_path

class Tester:
    def __init__(self, options: Options):

        """ Init Tester object with options parameters"""
        self.url = options.url
        self.department = options.department
        self.country = options.country
        self.city = options.city
        self.state = options.state
        self.num_jobs_to_compare = options.num_jobs_to_compare
        self.init_driver(options.driver_path)

    def init_driver(self, driver_path):
        service = Service(executable_path = driver_path)
        self.driver = webdriver.Chrome(service = service)
        
        pass

    def open_browser(self):
        # some code to scrape the website
        self.driver.get(self.url)
        self.driver.maximize_window()
        
        pass

    def close_browser(self):
        self.driver.quit()
        pass
    
    def get_city_togglers(self):
        """ 
        Get all dropdowns for city, state and country 
        As they have the same css id, get_city_togglers will return all of them
        and we will use the indexes to select the correct one
        If a country with a state is selected (eg. USA) there is one more dropdown for the state
        """
        return  self.driver.find_elements(By.XPATH, TOGGLER_ID_XPATH_SELECTOR)
        

    def get_scroll_area(self):
        """
        After clicking a dropdown, a div with a scrollable area will appear with the options
        As most options are hidden, we need to scroll to the bottom to make them visible and select them
        This method will return all scrollable areas. As we select the department first, the first scrollable area will be the department
        and so on, so we can use the indexes to select the correct one
        """
        return  self.driver.find_elements(By.XPATH, SCROLL_AREA_XPATH_SELECTOR)
    
    def click_department_toggler(self):
        """ 
        The department dropdown is the first one, and the only one with a unique css id, so we can click it directly
        """
        toggler = self.driver.find_element(By.ID, DEPARTAMENT_TOGGLER_CSS_ID)
        toggler.click()
        return


    def select_department(self):
        """
        This method will scroll the options area, select the department from the dropdown and click it when becomes visible
        """
        self.click_department_toggler()
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
        """
        This method will select the country from the dropdown, and click it when becomes visible
        Country toggler is always the first so we can use the index 0 defined as a constant to select it
        """
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
        """
        This method will select the state from the dropdown, and click it when becomes visible
        State toggler is only visible if the country selected is USA and it is the second dropdown
        We can use the index 1 defined as a constant to select it
        """
        toggler = self.get_city_togglers()[STATE_TOGGLER_IDX]
        toggler.click()

        area = self.get_scroll_area()[STATE_SCROLLAREA_IDX]

        for i in range(10):
            self.driver.execute_script("arguments[0].scrollBy(0,200);", area) 
            try:    
                state_option = self.driver.find_element(By.LINK_TEXT, self.state)
                state_option.click()
                break
            except Exception as e:
                continue 
        

    def select_city_with_state(self):
        """
        This method will select the city from the dropdown, and click it when becomes visible
        City toggler is the third dropdown, and the second if the country selected is USA
        We can use the index 2 defined as a constant to select it
        All the logic to decide if the city is in the USA or not is done in the scrape method
        """
        self.get_city_togglers()[WITH_STATE_CITY_TOGGLER_IDX].click()

        area = self.get_scroll_area()[WITH_STATE_CITY_SCROLLAREA_IDX]
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
        """
        This method will select the city from the dropdown, and click it when becomes visible
        City toggler is the second dropdown, and the first if the country selected is USA
        We can use the index 1 defined as a constant to select it
        All the logic to decide if the city is in the USA or not is done in the scrape method
        """
        self.get_city_togglers()[WITHOUT_STATE_CITY_TOGGLER_IDX].click()

        area = self.get_scroll_area()[WITHOUT_STATE_CITY_SCROLLAREA_IDX]
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
        """
        This method will click the search button to display the jobs
        """

        self.driver.find_element(By.XPATH, SEARCH_BUTTON_XPATH_SELECTOR).click()
        pass
    
    def set_available_jobs_list(self):
        """
        This method will set the available jobs list to be compared with the expected number of jobs
        The tricky part here is that there is multiple main divs with the same class name that handles different media queries
        And inside each divs there are two divs with the job cards but only one is displayed
        We need to select the correct one to get the job cards based on screen size
        As the requeriment demanded to maximize the window, we can use the div related to the large screen
        """
        self.job_list = self.driver.find_elements(By.XPATH, JOB_CARD_XPATH_SELECTOR)
        
    
    def scrape(self):
        """
        This method will call all the methods to scrape the website and set the available jobs list
        and define the logic to select the city based on the country and state
        """

        self.open_browser()
        self.select_department()
        self.select_country()
        if self.state:
            self.select_state()
            self.select_city_with_state()

        else:
            self.select_city_without_state()

        self.click_search_button()
        
        self.set_available_jobs_list()

    def jobs_found_match_expected(self):
        """
        Return a bool that indicates if the number of jobs found is the same as the expected
        """
        return len(self.job_list) == self.num_jobs_to_compare
    
    def run(self):
        """
        Entry point to the script
        Execute the test and logs the result
        """
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