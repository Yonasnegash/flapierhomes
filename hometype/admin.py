from django.contrib import admin

from .models import HomeType

class HomeTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'register_date')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 25

admin.site.register(HomeType, HomeTypeAdmin)
