from django.contrib.auth.models import User
from Habit.models import Habit
from Day.models import Day
from django.dispatch import receiver
from django.db.models.signals import post_save

@receiver(post_save, sender=Habit)
def create_days(sender, instance, created, *args, **kwargs):
    if created:
        print(instance)
        delta_time = (instance.end_date - instance.start_date).days
        print(delta_time)
        for number in range(0, delta_time):
            print(number)
            Day.objects.create(habit=instance).save()

post_save.connect(create_days, sender=Habit)