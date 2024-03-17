import scraper
import json
import time
from multiprocessing.pool import ThreadPool as Pool
from pathlib import Path

class Test:

    def __init__(
        self, 
        headless = False, 
        processes = 1, 
        config = None,
        ):
        self.headless = headless
        self.processes = processes
        self.config = config
        """ Messages """
        self.config_log_message =f"\n\tRunning test with {self.processes} processes\n\tHeadless mode set to: {self.headless}"
        self.config_file_not_found_message =f"\n\tFile '{self.config}' not found\n\tPlease provide a valid file path and try again\n\tExiting Program..."
        self.default_test_message ="\n\tNo config file provided, running default test with Romania and USA scope"
    def check_config_file(self):
        path_to_config_file = Path(self.config)
        # If config file is not valid or does not exist, exit with a message
        if not path_to_config_file.exists():
            print(self.config_file_not_found_message)
            exit(1)
        return
        
    def parse_config_file(self):
        self.check_config_file()
        tests_options = []
        ## Load Json
        with open(self.config, 'r') as file:
            config_data = json.load(file)
            file.close()
        for config in config_data:    
            options = scraper.Options(
                    department=config['department'],
                    country=config['country'],
                    state=config['state'],
                    city=config['city'],
                    num_jobs_to_compare=config['num_jobs_to_compare'],
                    headless=self.headless)
            tests_options.append(options)

        return tests_options
    
    def define_test_scope(self):
        if self.config:
            tests_options = self.parse_config_file()
            return tests_options
        else:
            print(self.default_test_message)
            romania_option = scraper.Options(
                        department="Sales",
                        country="Romania",
                        city="Bucharest",
                        num_jobs_to_compare=28,
                        headless=self.headless)
            usa_option = scraper.Options(
                                    department="Sales",
                                    country="USA",
                                    state="Texas",
                                    city="Austin",
                                    num_jobs_to_compare=1,
                                    headless=self.headless)
            tests_options = [romania_option, usa_option]
            return tests_options
    
    def run(self):
        print(self.config_log_message)
        start = time.perf_counter()
        pool = Pool(self.processes)
        tests_options =  self.define_test_scope()
        for test_option in tests_options:
            tester = scraper.Tester(test_option)
            pool.apply_async(tester.run)
        pool.close()
        pool.join()
        duration = time.perf_counter() - start
        print(
        f"""
        Test completed in {duration:0.4f} seconds
        """)
        exit(1)
        return





