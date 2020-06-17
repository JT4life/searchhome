from django.contrib import admin
from .models import Property, SendMessage, Agent
# Register your models here.
class HomeAdmin(admin.ModelAdmin):
    list_display = ('name','type_home_choices','details','location','address','price','purpose')
    list_filter = ('created','name','price',)
    search_fields = ('price','name','location')
    ordering = ['created',]

admin.site.register(Property, HomeAdmin)
admin.site.register(SendMessage)
admin.site.register(Agent)
