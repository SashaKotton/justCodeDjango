from django.contrib import admin
from Orders.models import Order, Payment

# Register your models here.
admin.site.register(Payment)
admin.site.register(Order)