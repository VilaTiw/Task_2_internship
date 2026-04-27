from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_welcome_email(user_email, username):
    subject = "Welcome to our system!"
    message = f"Hello {username}! You have successfully registered."
    from_email = "admin@task_2.com"

    send_mail(subject, message, from_email, [user_email])
