from django.contrib import admin
from .models import Hub,State,CentralHub

# Register your models here.
class CentralHubAdmin(admin.ModelAdmin):
    list_display = ('state', 'city')

class HubAdmin(admin.ModelAdmin):
    list_display = ('city', 'address', 'central_hub')

admin.site.register(State)
admin.site.register(Hub, HubAdmin)
admin.site.register(CentralHub, CentralHubAdmin)