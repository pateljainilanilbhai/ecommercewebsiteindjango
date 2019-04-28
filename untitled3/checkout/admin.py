from django.contrib import admin
from .models import Order, OrderLineItem
from contact.models import Query



class OrderLineAdminInline(admin.TabularInline):
    model = OrderLineItem

class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineAdminInline, )
    
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderLineItem)
admin.site.register(Query)