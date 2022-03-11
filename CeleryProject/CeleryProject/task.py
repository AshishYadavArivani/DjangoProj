from celery import shared_task
import celery
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from CeleryProject import settings
from email.message import EmailMessage
import smtplib

@shared_task(bind=True)
def test_func(self):
    #operation
    for i in range(11):
        print(i)
    return "done"

@shared_task(bind=True)
def send_mail_func(self):
    # send_mail(
    #     subject="This is testing mail by django celery",
    #     message="This message from django selery for testing....",
    #     from_email=settings.EMIAL_HOST_USER,
    #     recipient_list=['ashishyadav800786@gmail.com'],
    #     fail_silently=False,

    # )

    msg = EmailMessage()
    # contacts = ["""asif@arivani.net", "amit@arivani.net", "saqib@arivani.com", "admin@arivani.com"]
    msg["From"] = 'repair.repairzoneusa@gmail.com'
    msg["To"] =   ["ashishyadav800786@gmail.com"] 
    msg["Subject"] = "MygeoTab Driver Report Test Mail"
    msg.set_content("Daily report scheduler")

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login('repair.repairzoneusa@gmail.com','Tech8866!@#')
        smtp.send_message(msg)
        print("Message Send Successfully !")




    return "Done.........."