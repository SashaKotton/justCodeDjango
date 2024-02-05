from django.db import models

# Create your models here.

class ingridient(models.Model):
    INGRIDIENT_TYPE = (
        ('meat','Мясо'),
        ('green','Зелень'),
    )

    type = models.CharField(verbose_name='Тип ингридиента', choices = INGRIDIENT_TYPE, max_length=255, default = 'meat')
    title = models.CharField(max_length=255, verbose_name='Ингридиенты')
    count_measure = models.CharField(max_length=255, verbose_name='Мера измерения')
    count = models.IntegerField(default=0, verbose_name='Количество')
    buy_price = models.IntegerField(default=0, verbose_name='Цена покупки')
    sell_price = models.IntegerField(default=0, verbose_name='Цена продажи')
    date_in = models.TimeField(verbose_name='Дата поступления на склад')

    class Meta:
        verbose_name='Ингридиент'
        verbose_name_plural = 'Ингридиенты'

    def __str__(self) -> str:
        return f'{self.pk} - {self.title}'