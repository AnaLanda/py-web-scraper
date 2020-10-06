import requests
import smtplib
import time
from bs4 import BeautifulSoup


def get_jobs():
    URL = 'https://djinni.co/jobs/keyword-java/'
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    return soup.findAll('div', class_='list-jobs__title')


def get_job_details():
    jobs = get_jobs()
    job_details = ""
    for job in jobs:
        title = job.find('a', class_='profile')
        href = job.find('a', href=True)
        job_details += title.text.strip() + ' https://djinni.co' + href['href'] + '\n'
    return job_details


# This method defines an SMTP client session object
# which is used to send mail to a Gmail email.
# Valid data must be set as the server.login()
# and server.sendmail() parameters for the code to work.
def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('sample_email@gmail.com', 'sample Google app password')
    subject = 'Active Java Vacancies'
    body = get_job_details()
    msg = f"Subject: {subject} \n\n{body}"
    server.sendmail(
        'from_sample_email@gmail.com',
        'to_sample_email@gmail.com',
        msg
    )
    print('Email has been sent')
    server.quit()


# Emails will be sent once a day (every 86,400 seconds).
while True:
    send_mail()
    time.sleep(86400)
