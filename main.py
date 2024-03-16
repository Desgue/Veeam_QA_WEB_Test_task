import scraper
import argparse
from pathlib import Path

def run_default_test():
    romania_options = scraper.Options(url="https://careers.veeam.com/vacancies",
                            department="Sales",
                            country="Romania",
                            city="Bucharest",
                            num_jobs_to_compare=28)
    usa_options = scraper.Options(url="https://careers.veeam.com/vacancies",
                            department="Sales",
                            country="USA",
                            state="Texas",
                            city="Austin",
                            num_jobs_to_compare=1)
    romania_tester = scraper.Tester(romania_options)
    usa_tester = scraper.Tester(usa_options)  

    romania_tester.run()
    usa_tester.run()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
                    prog='Veem Jobs Scraper',
                    description='Test the Veeam jobs page and verify the number of jobs in a specific department and location',
                    epilog='Created by: Eduardo Guedes')          
    parser._optionals.title = 'Optional arguments'
    
    parser.add_argument("-c", "--config", metavar="", help="Config JSON file path to configure tests scope, if no file is provided the test will run with the required scope of Romania and USA", type=str)
    args = parser.parse_args()

    if not args.config:
        run_default_test()
        exit(0)






