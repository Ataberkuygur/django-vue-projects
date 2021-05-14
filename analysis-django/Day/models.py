from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from Habit.models import Habit
from Category.models import Category

class Day(models.Model):
    day_number = models.PositiveIntegerField(default=1, editable=False)
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE, related_name='days')
    quantity = models.PositiveIntegerField(default=0)
    done = models.BooleanField(default=False)
    create_time = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True, editable=False)

    def get_day_number(self):
        number = 1
        while Day.objects.filter(habit=self.habit, day_number=number).exists():
            number += 1
        return number

    def get_unique_slug(self):
        number = 0
        slug = slugify(self.habit.title.replace('ı', 'i') + '-day-' + str(self.day_number))
        unique_slug = slug
        while Day.objects.filter(slug=unique_slug).exists():
            number += 1
            unique_slug = slugify(slug, number)
        return unique_slug

    def __str__(self):
        return f'{self.habit.title} - Day: {self.day_number}'

    def save(self, *args, **kwargs):
        if self.id is None:
            self.day_number = self.get_day_number()
            self.slug = self.get_unique_slug()
        return super(Day, self).save(*args, **kwargs)        

