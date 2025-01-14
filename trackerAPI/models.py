from django.db import models
from .managers import BookQueryset
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ['name']

class Publisher(models.Model):
    name = models.CharField(max_length=200, db_index=True)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        ordering = ['name']
    
class Book(models.Model):
    title = models.CharField(max_length=200, db_index=True)
    subtitle = models.CharField(max_length=200, null=True)
    authors = models.CharField(max_length=200)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    published_date = models.DateField(null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    distribution_expense = models.DecimalField(null=False, max_digits=5, decimal_places=2)

    objects = BookQueryset.as_manager()

    
    def __str__(self): 
        return self.title

    class Meta:
        ordering = ['title']

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.user.username} - {self.book.title}'

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite = models.ForeignKey(Favorite, on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ['user']

    def __str__(self):
        return self.user.username
    
@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
        UserProfile.objects.get_or_create(user=instance)

