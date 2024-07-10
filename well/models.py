from django.db import models


from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Well(models.Model):
    title = models.CharField(max_length=150, verbose_name='название')
    image = models.ImageField(upload_to="blog", verbose_name='изображение', **NULLABLE)
    content = models.TextField(verbose_name='содержание', **NULLABLE)

    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='well_owner', **NULLABLE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'выпускной блок'
        verbose_name_plural = 'выпускные блоки'
