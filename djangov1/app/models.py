from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class BookSwap(models.Model):
    title = models.CharField('Название', max_length=50)
    author = models.CharField('Автор', max_length=40)
    desc = models.TextField('Описание', max_length=255)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'