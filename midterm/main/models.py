from django.db import models
from utils.constants import TYPE_CHOICES


# Create your models here.

class BookJournalBase(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True, verbose_name='Название')
    price = models.IntegerField(default=0, verbose_name='Цена')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    created_at = models.DateField(verbose_name='Дата создания')

    class Meta:
        ordering = ['name']
        abstract = True


class Book(BookJournalBase):
    num_pages = models.IntegerField(default=0, verbose_name='Количество страниц')
    genre = models.CharField(max_length=255, null=True, blank=True, verbose_name='Жанр')

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'


class Journal(BookJournalBase):
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, default='Travel', verbose_name='Тип')
    publisher = models.CharField(max_length=255, null=True, blank=True, verbose_name='Издатель')

    class Meta:
        verbose_name = 'Журнал'
        verbose_name_plural = 'Журналы'
