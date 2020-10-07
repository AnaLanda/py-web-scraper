# Web Scraper for a Job Search Website

A program for crawling and scraping a job site (Djinni)
for the latest Java Developer vacancies. When run, the
program will send you an email every day with the top
latest vacancies that would usually show up on the first
page for the job category.

## Running the Project

To run the project on your local machine, you need to
- download the web-scraper.py file
- make sure you have Python 3 on your machine, which you could check by running 'python -v' command in your command line
- install the Python packages bs4, time, smtplib, and requests, e.g. by running 'pip3 install bs4' in your command line
- insert a real Gmail email and a valid Google app password for your device in the server.login() and server.sendmail() functions in web-scraper.py
- run the project in your command line by navigating to the folder with the downloaded web-scraper.py file and running the command 'python3 web-scraper.py'

## Libraries

 - BeautifulSoup
 - requests
 - smtplib
 - time

## Requirements

 - python 3.6+
 - pip dependencies
