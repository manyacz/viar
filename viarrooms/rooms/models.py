from django.db import models
from django.urls import reverse

class Rooms(models.Model):
    title = models.CharField(max_length=150, verbose_name='Номер комнаты')
    content = models.TextField(blank=True, verbose_name='Контент')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото', blank=True)
    price = models.IntegerField(verbose_name='Цена комнаты',)
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    # reserve =  models.ForeignKey('Reserve', on_delete=models.PROTECT, verbose_name='Резервация')
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
        
# class Reserve(models.Model):
#     title = models.ForeignKey(Rooms, on_delete=models.PROTECT)
#     date_in = models.DateField(verbose_name='Занято с')
#     date_out = models.DateField(verbose_name='Занято по')

    
    # class Meta:
    #     verbose_name = 'Резервация'
    #     verbose_name_plural = 'Резервации'
    #     ordering = ['title']