from django.db import models

# Create your models here.

class Payment(models.Model):
    title = models.CharField(max_length=255, verbose_name='Вариант платежа')

    class Meta:
        verbose_name='Вариант платежа'
        verbose_name_plural='Варианты платежа'

    def __str__(self):
        return self.title

class Order(models.Model):
    payment = models.ForeignKey(Payment, null = True, blank = True, verbose_name='Вариант платежа', on_delete= models.CASCADE)
    title = models.CharField(max_length=255, verbose_name = 'Заказы')
    total_price = models.IntegerField(default = 0, verbose_name = 'Итоговая цена')

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
    
    def __str__(self) -> str:
        return self.title
