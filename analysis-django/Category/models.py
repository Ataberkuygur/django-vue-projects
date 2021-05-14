from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

class Category(models.Model):
    title = models.CharField(max_length=50)
    daily_goal_type = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='categories')
    create_date = models.DateTimeField(auto_now=True)
    update_date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, editable=False)

    def get_unique_slug(self):
        number = 0
        slug = slugify(self.title.replace('ı', 'i') + ' ' + self.user.username.replace('ı', 'i'))
        unique_slug = slug
        while Category.objects.filter(slug=unique_slug).exists():
            number += 1
            unique_slug = slugify(slug, number)
        return unique_slug

    def __str__(self):
        return str(self.title)

    def save(self, *args, **kwargs):
        if self.id is None:
            self.slug = self.get_unique_slug()
        return super(Category, self).save(*args, **kwargs)        