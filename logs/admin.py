from django.contrib import admin
from .models import DriverLog, TruckChecklist, TruckImage, ThermoKingImage, InventoryItem

class TruckChecklistInline(admin.StackedInline):
    model = TruckChecklist
    extra = 0

class TruckImageInline(admin.TabularInline):
    model = TruckImage
    extra = 0

class ThermoKingImageInline(admin.TabularInline):
    model = ThermoKingImage
    extra = 0

@admin.register(DriverLog)
class DriverLogAdmin(admin.ModelAdmin):
    list_display = ['user', 'truck', 'start_datetime', 'end_datetime', 'created_at']
    list_filter = ['truck', 'start_datetime', 'user']
    search_fields = ['user__username', 'work_description', 'error_lights_faults']
    inlines = [TruckChecklistInline, TruckImageInline, ThermoKingImageInline]

@admin.register(TruckChecklist)
class TruckChecklistAdmin(admin.ModelAdmin):
    list_display = ['log', 'lights', 'mirrors', 'tires', 'brakes']
    list_filter = ['lights', 'mirrors', 'tires', 'brakes']

@admin.register(TruckImage)
class TruckImageAdmin(admin.ModelAdmin):
    list_display = ['log', 'image_type', 'uploaded_at']
    list_filter = ['image_type', 'uploaded_at']

@admin.register(ThermoKingImage)
class ThermoKingImageAdmin(admin.ModelAdmin):
    list_display = ['log', 'image_type', 'uploaded_at']
    list_filter = ['image_type', 'uploaded_at']

@admin.register(InventoryItem)
class InventoryItemAdmin(admin.ModelAdmin):
    list_display = ['log', 'airway_bill', 'item_type', 'amount_small', 'amount_large', 'total_items', 'description']
    list_filter = ['item_type']
    search_fields = ['airway_bill', 'description']
    
    def total_items(self, obj):
        return obj.amount_small + obj.amount_large
    total_items.short_description = 'Total Items'