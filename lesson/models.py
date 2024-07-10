from django.db import models

from users.models import User
from well.models import Well

NULLABLE = {'blank': True, 'null': True}


# Create your models here.
class Lesson(models.Model):
    title = models.CharField(max_length=200, verbose_name='название')
    description = models.TextField(verbose_name='описание')
    image = models.ImageField(upload_to="blog", verbose_name='изображение', **NULLABLE)
    link_to_video = models.TextField(verbose_name='ссылка на видео', **NULLABLE)
    well = models.ForeignKey(Well, on_delete=models.CASCADE, verbose_name='курс', **NULLABLE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='lesson_owner', **NULLABLE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
