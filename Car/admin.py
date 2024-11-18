from django.contrib import admin

from Car.models import Car, Comment, Manufacturer, Country

# Register your models here.


admin.site.register(Car)
admin.site.register(Comment)
admin.site.register(Manufacturer)
admin.site.register(Country)
