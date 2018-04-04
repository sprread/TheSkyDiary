from django.contrib import admin

# Register your models here.
from .models import Skies, Customer, Orders, Order_items, Request

admin.site.register(Skies)
admin.site.register(Customer)
admin.site.register(Orders)
admin.site.register(Order_items)
admin.site.register(Request)