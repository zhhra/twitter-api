from config.celery import app
from django.core.mail import EmailMessage
from django.urls import reverse
from helpers.otp import generateOTP
from django.core.cache import cache


@app.task(name="activation_email")
def send_activation_email(username, email, *args, **kwargs):
    while 1:
        password = generateOTP()
        if password not in cache:
            cache.set(password, username, timeout=120)
            break

    subject = "Twitter Account Activation"
    message = f"""
    your OTP:
    {password}  
    enter the above code in the link below:
    http://127.0.0.1:8000{reverse("auth:email_verification")}
    
    """
    to_email = email
    email = EmailMessage(subject, message, to=[to_email])
    email.send()
