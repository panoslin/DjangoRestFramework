from django.db import models
from django.contrib.auth.models import AbstractUser
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from pathlib import Path
from smtplib import SMTPSenderRefused
from concurrent import futures


class User(AbstractUser):
    staff_id = models.IntegerField(null=True)

    def email_staff(self):
        """
        send a notification email to this user

        https://docs.djangoproject.com/en/4.0/topics/email/#send-mail

        """
        # send email in the background
        executor = futures.ThreadPoolExecutor()
        executor.submit(self.__email_staff)
        executor.shutdown(wait=False)  # don't wait for the thread to finishes

    def __email_staff(self):
        subject = "Test Subject"
        tmp_path = Path(__file__).parent.joinpath('templates', 'staff_notification.html')
        tmp_context = {'name': self.username}
        html_msg = render_to_string(tmp_path, tmp_context)
        plain_msg = strip_tags(html_msg)
        try:
            self.email_user(
                subject=subject,
                message=plain_msg,
                from_email='sender.email@somewhere.com',
                html_message=html_msg,
            )
        except SMTPSenderRefused:
            # do something else
            pass