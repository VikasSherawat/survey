import threading
from polls import settings
from django.core.mail import send_mail,EmailMultiAlternatives


class EmailThread(threading.Thread):

    def __init__(self, recipient_list,message):
        self.recipient_list = recipient_list
        self.message = message
        threading.Thread.__init__(self)

    def run (self):
        subject = 'Poll participation Link'
        # send_mail(
        #     subject,
        #     self.message,
        #     settings.EMAIL_HOST_USER,
        #     self.recipient_list,
        #     fail_silently=False,
        # )

        msg = EmailMultiAlternatives(subject, self.message, settings.EMAIL_HOST_USER, self.recipient_list)
        msg.content_subtype = "html"
        msg.send()