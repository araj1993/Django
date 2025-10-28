from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Product, Order, OrderProduct


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    """
    Custom User admin interface for simplified User model.
    """
    list_display = ('username', 'email', 'is_staff', 'is_active', 'date_joined')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'date_joined')
    search_fields = ('username', 'email')
    ordering = ('username',)
    
    # Custom fieldsets for our simplified User model
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Contact info', {'fields': ('email',)}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    
    # For creating new users
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2'),
        }),
    )


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """
    Product admin interface.
    """
    list_display = ('name', 'price', 'stock', 'is_in_stock', 'created_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('name', 'description')
    list_editable = ('price', 'stock')
    readonly_fields = ('created_at', 'updated_at')
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'description')
        }),
        ('Pricing & Stock', {
            'fields': ('price', 'stock')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    def is_in_stock(self, obj):
        return obj.is_in_stock
    is_in_stock.boolean = True
    is_in_stock.short_description = 'In Stock'


class OrderProductInline(admin.TabularInline):
    """
    Inline interface for order items within the order admin.
    """
    model = OrderProduct
    extra = 1
    readonly_fields = ('subtotal',)
    
    def subtotal(self, obj):
        if obj.id:
            return f"${obj.subtotal:.2f}"
        return "—"
    subtotal.short_description = 'Subtotal'


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """
    Order admin interface with inline order items.
    """
    list_display = ('id', 'user', 'order_date', 'status', 'total_amount', 'item_count')
    list_filter = ('status', 'order_date')
    search_fields = ('user__username', 'user__email')
    readonly_fields = ('order_date', 'total_amount')
    inlines = [OrderProductInline]
    
    fieldsets = (
        ('Order Information', {
            'fields': ('user', 'status')
        }),
        ('Order Details', {
            'fields': ('order_date', 'total_amount'),
            'classes': ('collapse',)
        }),
    )
    
    def item_count(self, obj):
        return obj.order_items.count()
    item_count.short_description = 'Items'
    
    def save_model(self, request, obj, form, change):
        """Override save to recalculate total when order is saved."""
        super().save_model(request, obj, form, change)
        obj.calculate_total()


@admin.register(OrderProduct)
class OrderProductAdmin(admin.ModelAdmin):
    """
    Order Product admin interface for direct management of order items.
    """
    list_display = ('order', 'product', 'quantity', 'price_at_time', 'subtotal')
    list_filter = ('order__status', 'order__order_date')
    search_fields = ('order__id', 'product__name', 'order__user__username')
    readonly_fields = ('subtotal',)
    
    def subtotal(self, obj):
        return f"${obj.subtotal:.2f}"
    subtotal.short_description = 'Subtotal'


# Customize admin site headers
admin.site.site_header = "E-commerce Admin"
admin.site.site_title = "E-commerce Admin Portal"
admin.site.index_title = "Welcome to E-commerce Administration"