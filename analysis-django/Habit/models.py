from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from Category.models import Category

class Habit(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=225, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='habits')
    success_rate = models.PositiveIntegerField(default=0)
    daily_goal = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='habits')
    start_date = models.DateField(auto_now=True)
    end_date = models.DateField()
    slug = models.SlugField(unique=True, editable=False)

    def get_unique_slug(self):
        number = 0
        slug = slugify(self.title.replace('ı', 'i') + ' ' + self.user.username.replace('ı', 'i'))
        unique_slug = slug
        while Habit.objects.filter(slug=unique_slug).exists():
            number += 1
            unique_slug = slugify(slug, number)
        return unique_slug
    
    def __str__(self):
        return str(self.title)

    def save(self, *args, **kwargs):
        if self.id is None:
            self.slug = self.get_unique_slug()
            print(self.slug)
        return super(Habit, self).save(*args, **kwargs)
