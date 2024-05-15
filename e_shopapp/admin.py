from django.contrib import admin
from e_shopapp.models import Contact, OrderUpdate, Orders, Product, User_details

# Register your models here.
admin.site.register(Contact)
admin.site.register(Product)
admin.site.register(Orders)
admin.site.register(OrderUpdate)
admin.site.register(User_details)
