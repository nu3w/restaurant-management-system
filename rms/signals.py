from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import Order


@receiver(post_save, sender=Order)
def order_post_save(sender, instance, created, **kwargs):
    if created:
        send_mail(
            subject="New Order Created",
            message="A new order has been created.",
            from_email="admin@example.com",
            recipient_list=["user@example.com"],
            fail_silently=False,
        )