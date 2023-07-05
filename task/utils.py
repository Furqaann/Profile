from django.core.mail import send_mail
from django.conf import settings

def send_mail_to_client(f_name,f_email,f_message):
    name=f_name
    sender_email=f_email
    message = f_message
    from_email=settings.EMAIL_HOST_USER
    receipient_list = ["furqanfiaz100@gmail.com"]
    send_mail(sender_email, message, name,  receipient_list)