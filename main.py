import scraper

if __name__ == '__main__':
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




