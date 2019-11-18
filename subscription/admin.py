from django.contrib import admin
from .models import Subscription

class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('email',)
    # list_display_links = ('id', 'email',)
    search_fields = ('email',)
    list_per_page = 25
    
admin.site.register(Subscription, SubscriptionAdmin)
