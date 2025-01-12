from django.db import models

# Create your models here.
from django.db import models

class AboutPage(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Контент")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Страница о нас"
        verbose_name_plural = "Страницы о нас"
