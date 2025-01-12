
# Create your models here.
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название")
    author = models.CharField(max_length=200, verbose_name="Автор")
    description = models.TextField(verbose_name="Описание")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    cover = models.ImageField(upload_to='book_covers/', verbose_name="Обложка", blank=True, null=True)
    published_date = models.DateField(verbose_name="Дата публикации")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"
