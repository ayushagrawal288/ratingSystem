from django.contrib import admin
from core.models import Product, UserProductMapping, Rating

admin.site.register(Product)
admin.site.register(UserProductMapping)
admin.site.register(Rating)
