from django.contrib import admin
from store.models import Pizza, Order, OrderItem, Ingredient


class PizzaAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'id')
    list_filter = ('ingredients', )
    readonly_fields = ['id', ]


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ['total_price', ]


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('pizza', 'quantity')
    fields = ('pizza', 'quantity', 'total_price')
    readonly_fields = ['total_price', ]


class OrderAdmin(admin.ModelAdmin):
    list_display = ('address', 'phone', 'comments', 'total_price')
    inlines = [OrderItemInline, ]
    readonly_fields = ['total_price', ]


admin.site.register(Ingredient)
admin.site.register(Pizza, PizzaAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
