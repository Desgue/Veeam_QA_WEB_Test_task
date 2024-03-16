import scraper
import argparse
from pathlib import Path

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


def run_test_with_config_file(config_file):
    test_options = scraper.Options.from_json(config_file)
    tester = scraper.Tester(test_options)
    tester.run()

if __name__ == '__main__':
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
        "-no--headless",
        help="Run the tests with browser view mode. If you want to run multiple tests I reccomend using --headless",
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


    print("""
 / \------------------------, 
 \_,|                       | 
    |    VEEAM ASSESSMENT   | 
    |  ,----------------------
    \_/_____________________/ 
    """)


    args = parser.parse_args()

    print("Headless mode set to: ", args.headless)

    if not args.config:
        print("No config file provided, running default test with Romania and USA scope")
        run_default_test(headless = args.headless)
        exit(1)
    
    path_to_config_file = Path(args.config)
    if not path_to_config_file.is_file():
        print(f"\nFile '{args.config}' not found")
        print("Please provide a valid file path and try again\n")
        exit(1)

    print(f"Running test with config file: {args.config}")
    run_test_with_config_file(args.config)



