from django.contrib import admin

from .models import RealEstate

class RealtestatesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'address', 'agent', 'register_date')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 25

admin.site.register(RealEstate, RealtestatesAdmin)
