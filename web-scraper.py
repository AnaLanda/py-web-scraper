import requests
import smtplib
import time
from bs4 import BeautifulSoup


def get_jobs():
    URL = 'https://djinni.co/jobs/keyword-java/'
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    print(soup.findAll('div', class_='list-jobs__title'))
    return soup.findAll('div', class_='list-jobs__title')


def get_job_details():
    jobs = get_jobs()
    job_details = ""
    for job in jobs:
        title = job.find('a', class_='profile')
        href = job.find('a', href=True)
        print('Job details gotten')
        job_details += title.text.strip() + ' https://djinni.co' + href['href'] + '\n'
    print(job_details)
    return job_details


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    # insert valid data for server login
    server.login('sample_email@gmail.com', 'sample Google app password')
    subject = 'Active Java Vacancies'
    body = get_job_details()
    msg = f"Subject: {subject} \n\n{body}"
    server.sendmail(
        'sample_email@gmail.com',
        'sample_email@gmail.com',
        msg
    )
    print('Email has been sent')
    server.quit()


while True:
    send_mail()
    # emails will be sent once a day
    time.sleep(86400)
