from django.db import models


class News(models.Model):
    """
    это модель описывает структуру новости в базе данных
    """

    title = models.CharField(max_length=50)
    desc = models.TextField(null=True, blank=True)    
    create_date = models.DateTimeField(auto_now_add=True)
    author= models.CharField(max_length=150)

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def __str__(self)-> str:
        return f'id:{self.id} {self.title}'