import scraper
import argparse
import json


def run_default_test(headless: bool):
    romania_options = scraper.Options(url="https://careers.veeam.com/vacancies",
                            department="Sales",
                            country="Romania",
                            city="Bucharest",
                            num_jobs_to_compare=28,
                            headless=headless)

    usa_options = scraper.Options(url="https://careers.veeam.com/vacancies",
                            department="Sales",
                            country="USA",
                            state="Texas",
                            city="Austin",
                            num_jobs_to_compare=1,
                            headless=headless)
    romania_tester = scraper.Tester(romania_options)
    usa_tester = scraper.Tester(usa_options)  

    romania_tester.run()
    usa_tester.run()


def run_test_with_config_file(path_to_config_file: str, headless: bool):
    config_data = parse_config_file(path_to_config_file)
    for config in config_data:
        options = scraper.Options(url=config['url'],
                            department=config['department'],
                            country=config['country'],
                            state=config['state'],
                            city=config['city'],
                            num_jobs_to_compare=config['num_jobs_to_compare'],
                            headless=headless)
        tester = scraper.Tester(options)
        tester.run()

def configure_arg_parser():
    parser = argparse.ArgumentParser(
                    prog='Veem Jobs Scraper',
                    description='Test the Veeam jobs page and verify the number of jobs in a specific department and location',
                    epilog='Created by: Eduardo Guedes')          

    parser._optionals.title = 'Optional arguments'

    parser.add_argument(
        "--headless",
        help="Run the tests in headless mode. If you want to run multiple tests set this to true",
        action="store_true",
        )
    parser.add_argument(
        "--no-headless",
        help="Run the tests with browser view mode. This is the default. If you want to run multiple tests I reccomend using --headless",
        action="store_false",
        )

    parser.add_argument(
        "-c", "--config", 
        metavar="", 
        help="""
        Configuration JSON file path to configure tests scope, if no file is provided the test will run with the required scope of Romania and USA.
        You may pass a list of options to test multiple locations and departments, but I would recommend to set -h false to run the tests in headless mode.
        """,
         type=str)
    parser.set_defaults(headless=False)
    return parser

def parse_config_file(config_file):
    ## Load Json
    with open(config_file, 'r') as file:
        config_data = json.load(file)
        file.close()
    return config_data
