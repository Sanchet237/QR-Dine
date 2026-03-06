from django.contrib import admin
from .models import Restaurant, Category, MenuItem


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'owner', 'email', 'is_active', 'created_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['name', 'email', 'owner__email']
    readonly_fields = ['slug', 'created_at', 'updated_at']
    fieldsets = (
        ('Basic Information', {
            'fields': ('owner', 'name', 'slug', 'email', 'phone')
        }),
        ('Details', {
            'fields': ('address', 'description', 'logo')
        }),
        ('Status', {
            'fields': ('is_active',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'restaurant', 'order', 'item_count', 'created_at']
    list_filter = ['restaurant', 'created_at']
    search_fields = ['name', 'restaurant__name']
    ordering = ['restaurant', 'order', 'name']


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'restaurant', 'category', 'price', 'is_available', 'created_at']
    list_filter = ['restaurant', 'category', 'is_available', 'created_at']
    search_fields = ['name', 'description', 'restaurant__name']
    readonly_fields = ['created_at', 'updated_at']
    fieldsets = (
        ('Basic Information', {
            'fields': ('restaurant', 'name', 'category')
        }),
        ('Details', {
            'fields': ('description', 'price', 'image')
        }),
        ('Availability', {
            'fields': ('is_available',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
