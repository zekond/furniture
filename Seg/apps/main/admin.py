from django.contrib import admin

from Seg.apps.main.models import Youth, Mattress, Diningroom, Livingroom, Bedroom, Home, Category

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name')

class YouthAdmin(admin.ModelAdmin):
    list_display = ('id','name')


class MattressAdmin(admin.ModelAdmin):
    list_display = ('id','name')

class LivingroomAdmin(admin.ModelAdmin):
    list_display = ('id','name')

class DiningroomAdmin(admin.ModelAdmin):
    list_display = ('id','name')

class BedroomAdmin(admin.ModelAdmin):
    list_display = ('id','name')

class HomeAdmin(admin.ModelAdmin):
    list_display = ('id','name')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Youth, YouthAdmin)
admin.site.register(Mattress, MattressAdmin)
admin.site.register(Diningroom,DiningroomAdmin)
admin.site.register(Livingroom, LivingroomAdmin)
admin.site.register(Bedroom, BedroomAdmin)
admin.site.register(Home, HomeAdmin)