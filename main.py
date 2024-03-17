from test import Test

import argparse
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

    parser.add_argument(
        "-p", "--processes",
        help="Run the tests concurrently. If you want to run multiple tests set this to true. Default is 1 process.  '-p 6' will run 6 processes concurrently.",
        type=int,
        )
    parser.set_defaults(headless=False, processes=1)
    return parser



def main():
    print(
    """
    / \ -----------------------, 
    \ ,|                       | 
       |    VEEAM ASSESSMENT   | 
       |  ,----------------------
       \ /_____________________/ 
    """)

    # Parse command line arguments
    parser = configure_arg_parser()
    args = parser.parse_args()

    is_headless = args.headless
    config = args.config 
    processes = args.processes

    test = Test(headless = is_headless, processes = processes, config = config)

    test.run()






if __name__ == '__main__':
    main()





