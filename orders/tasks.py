from celery import shared_task
from django.core.mail import send_mail
from .models import Order


@shared_task
def order_created(order_id):
    order = Order.objects.get(id=order_id)
    subject = f'Order nr. {order.id}'
    message = (f'Dear {order.first_name}, \n\n'
               f'Your have successfully placed an order.\n\n'
               f'Your order ID is {order.id}\n\n.'
               )
    mail_sent = send_mail(subject, message, "admin@myshop.com", [order.email])
    return mail_sent

