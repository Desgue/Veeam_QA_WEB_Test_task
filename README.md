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

## Installation and Running
Make sure you have python and pip updated to latest version

1. Clone the repository
```
git clone https://github.com/Desgue/Veeam_QA_WEB_Test_task.git
```

2- Install selenium (only dependencie)
```
pip install selenium
```
3- On root folder run
```
python main.py
```

## Usage
1. On main.py create a options object to define your test settings. 
   ```
       options = scraper.Options(url="https://careers.veeam.com/vacancies",
                            department="Sales",
                            country="Romania",
                            city="Bucharest",
                            num_jobs_to_compare=28)
   ```
The variable **num_of_jobs_to_compare** is what we are testing the website against. A sucessfull test means the script sucessfully collected all jobs listed for a particular department, country and city.

2. Inject the Options instance in a Tester instance
   ```
   romania_tester = scraper.Tester(romania_options)
   ```
3. Call the run method
   ```
   romania_tester.run()
   ```
The script should test if the number of available jobs is the same as the number of displayed jobs collected from the website.

The scripts logs the result of the comparison after it finishs running.

## Features on Development
1. Accept a file input with multiple config objects to perform batches of tests
2. Log results to a .log file for easier debugging and analysis
3. Accept a flag for running multiple tests in parallel
4. Accept a flag to toggle between running headless or not

   
