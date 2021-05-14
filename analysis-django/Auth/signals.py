from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=User)
def create_token(sender, instance, created, *args, **kwargs):
    if created:
        token = Token.objects.create(user=instance)
        token.save()

post_save.connect(create_token, sender=User)