from django.db import models

# Create your models here.
class Blog(models.Model):
    image = models.ImageField(
        upload_to='image/'
    )
    title = models.CharField(
        max_length=255,
        verbose_name='Заголовок'
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    def __str__(self) -> str:
        return self.title
    class Meta:
        verbose_name = 'Запись блога'
        verbose_name_plural = 'Записи блога'