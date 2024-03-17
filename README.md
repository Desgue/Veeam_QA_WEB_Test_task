# Veeam Junior QA Assessment

## Requeriments
- Open https://careers.veeam.com/vacancies and maximize the browser window.
- Then, using the jobs filter on the page, count the number of Sales positions in two locations:
  - Romania, Bucharest
  - USA, Texas, Austin
    
- You are expected to count positions by choosing the correct filter settings, pressing search
button and counting blocks that represent open positions.

- Compare the number of positions with the expected result for each location.

**Notes:**

It would be a good idea to parametrize the values of input parameters and the expected job
number so that the code could be used with various parameter sets.
You can use a browser of your choice.

Please do not use ChatGPT or similar tools.

## Installation
Make sure you have python and pip updated to latest version

1. Clone the repository
```
git clone https://github.com/Desgue/Veeam_QA_WEB_Test_task.git
```

2- Install selenium (only 3rd party dependency)
```
pip install selenium
```


## Usage

**Command Syntax** 

To test only the main requirements demanded, run
```
python main.py
```

Optionally you can pass arguments to provide a Json file with additional test cases, set headless mode and set the number of processes used to run the script.
All defaults are set so the script tests the main requirements only. 
All options can be set interchangeably and none is required for the program to run.
```
python main.py [--option]
```

### Optional Arguments


#### `-h`, `--help`
- Description: Show the help menu that indicates what each command does and how to use it.
- Usage: `-h` or `--help` 

#### `--headless`
- Description: Run the tests in headless mode. If enabled, the browser window will not be visible during testing.
- Usage: `--headless`
- Default: False

#### `--no-headless`
- Description: Run the tests with browser view mode. This is the default behavior.
- Usage: `--no-headless`

#### `-c`, `--config`
- Description: Specify a configuration JSON file path to configure test scope. If not provided, tests will run with the default scope of Romania and USA.
- Usage: `-c <path_to_config_file.json>` or `--config <path_to_config_file.json>`
- Default: None

#### `-p`, `--processes`
- Description: Specify the number of processes to be run concurrently.
- Usage: `-p <number of processes>` or `--processes <number of processes>` 
- Default: 1

#### Json format
```json
[
    {
        "department": "Sales",
        "country": "Romania",
        "state": "",
        "city": "Bucharest",
        "num_jobs_to_compare": 28
    },
    {
        "department": "Sales",
        "country": "USA",
        "state": "Texas",
        "city": "Austin",
        "num_jobs_to_compare": 1
    }
]
```

### Example
```python
python main.py --headless --config test_cases.json --processes 10
```
Will selenium on headless mode, load the test cases provided with the Json file and will max out the process at 10 if needed.

### File structure
1. main.py - The entry point of the program, parses the arguments, construct the object and call the run method.
2. scraper.py - Is where the core logicof the program is, it defines two classes Options and Tester, options is responsible for holding all the configuration options for the scraping, to be injected into the Tester class, that in its turn will perform the website scraping and compare te results to the provided expected result.
3. test.py - Defines a Test class that is responsible for holding the configuration for the Test and perform logic based on the Command Line arguments provided. It constructs the Options and Tester objects and holds the logic necessary to call the Tester.run() method.
4. test_cases.json - Is a json file with different test scenarios used to assert the script is working under different conditions.
5. misc/old_code.py - Is the POC code developed with comments made during the process.
6. chormedriver.exe - Is the driver choosen for selenium. 



## Features on Development
1. ~~Accept a file input with multiple config objects to perform batches of tests~~
2. ~~Accept a flag to toggle between running headless or not~~
3. ~~Accept a flag for running multiple tests in parallel~~
4. Log results to a .log file for easier debugging and analysis

   
