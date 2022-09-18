from django.db import models
from django.urls import reverse
from photologue.models import ImageModel, Photo

class Rooms(models.Model):
    title = models.CharField(max_length=150, verbose_name='Номер комнаты')
    content = models.TextField(blank=True, verbose_name='Контент')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото', blank=True)
    # photo = models.ForeignKey('photologue.Photo', null=True, blank=True, on_delete=models.SET_NULL,)
    price = models.IntegerField(verbose_name='Цена комнаты',)
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    date_start = models.DateField(verbose_name='Занято с', blank=True, auto_now=False )
    date_end = models.DateField(verbose_name='Занято по', blank=True, auto_now=False) 
    
    
    def get_absolute_url(self):
        return reverse('view_rooms', kwargs={'pk': self.pk}) 
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Комната'
        verbose_name_plural = 'Комнаты'
        ordering = ['title']