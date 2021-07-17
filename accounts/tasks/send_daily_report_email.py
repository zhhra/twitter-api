from config.celery import app
from django.core.mail import send_mail
from accounts.models.user import User


@app.task(name="send_daily_report_email")
def send_daily_report_email():
    for user in User.objects.filter(is_active=True):
        subject = "daily report"
        message = f"""Hi, your daily report:

            """
        email_from = "zahra"
        recipient_list = [
            user.email,
        ]
        send_mail(subject, message, email_from, recipient_list)
