from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class DriverLog(models.Model):
    TRUCK_CHOICES = [
        ('hino_24', 'Hino24'),
        ('international_24', 'International24'),
        ('freightliner_26', 'Freightliner26'),
        ('hino_26', 'Hino26'),
    ]
    
    FUEL_LEVEL_CHOICES = [
        ('empty', 'Empty'),
        ('quarter', '1/4'),
        ('half', '1/2'),
        ('three_quarters', '3/4'),
        ('full', 'Full'),
    ]
    
    DEF_LEVEL_CHOICES = [
        ('empty', 'Empty'),
        ('quarter', '1/4'),
        ('half', '1/2'),
        ('three_quarters', '3/4'),
        ('full', 'Full'),
    ]
    
    INVENTORY_AMOUNT_CHOICES = [
        ('none', 'None'),
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    work_description = models.TextField()
    
    truck = models.CharField(max_length=20, choices=TRUCK_CHOICES)
    truck_mileage = models.PositiveIntegerField()
    truck_fuel_level = models.CharField(max_length=20, choices=FUEL_LEVEL_CHOICES)
    def_level = models.CharField(max_length=20, choices=DEF_LEVEL_CHOICES)
    thermoking_hours = models.PositiveIntegerField()
    error_lights_faults = models.TextField(blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.truck} - {self.start_datetime.date()}"

    def get_absolute_url(self):
        return reverse('log_detail', kwargs={'pk': self.pk})

class TruckChecklist(models.Model):
    CHECKLIST_CHOICES = [
        ('ok', 'OK'),
        ('needs_attention', 'Needs Attention'),
        ('not_applicable', 'N/A'),
    ]
    
    log = models.OneToOneField(DriverLog, on_delete=models.CASCADE, related_name='checklist')
    
    lights = models.CharField(max_length=20, choices=CHECKLIST_CHOICES, default='ok')
    mirrors = models.CharField(max_length=20, choices=CHECKLIST_CHOICES, default='ok')
    tires = models.CharField(max_length=20, choices=CHECKLIST_CHOICES, default='ok')
    brakes = models.CharField(max_length=20, choices=CHECKLIST_CHOICES, default='ok')
    suspension_check = models.CharField(max_length=20, choices=CHECKLIST_CHOICES, default='ok')
    pallet_jack = models.CharField(max_length=20, choices=CHECKLIST_CHOICES, default='ok')
    shrink_wrap = models.CharField(max_length=20, choices=CHECKLIST_CHOICES, default='ok')
    pallets = models.CharField(max_length=20, choices=CHECKLIST_CHOICES, default='ok')
    def_fluid = models.CharField(max_length=20, choices=CHECKLIST_CHOICES, default='ok')
    
    notes = models.TextField(blank=True, null=True)

class TruckImage(models.Model):
    IMAGE_TYPE_CHOICES = [
        ('truck_front', 'Truck Front'),
        ('truck_back', 'Truck Back'),
        ('truck_left', 'Truck Left'),
        ('truck_right', 'Truck Right'),
        ('truck_interior', 'Truck Interior'),
        ('truck_dashboard', 'Truck Dashboard'),
    ]
    
    log = models.ForeignKey(DriverLog, on_delete=models.CASCADE, related_name='truck_images')
    image_type = models.CharField(max_length=20, choices=IMAGE_TYPE_CHOICES)
    image = models.ImageField(upload_to='truck_images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

class ThermoKingImage(models.Model):
    IMAGE_TYPE_CHOICES = [
        ('thermoking_front', 'ThermoKing Front'),
        ('thermoking_side', 'ThermoKing Side'),
        ('thermoking_controls', 'ThermoKing Controls'),
    ]
    
    log = models.ForeignKey(DriverLog, on_delete=models.CASCADE, related_name='thermoking_images')
    image_type = models.CharField(max_length=20, choices=IMAGE_TYPE_CHOICES)
    image = models.ImageField(upload_to='thermoking_images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

class InventoryItem(models.Model):
    INVENTORY_TYPE_CHOICES = [
        ('culantro', 'Culantro'),
        ('thyme', 'Thyme'),
        ('empty_boxes', 'Empty boxes'),
        ('other', 'Other'),
    ]
    
    log = models.ForeignKey(DriverLog, on_delete=models.CASCADE, related_name='inventory_items')
    airway_bill = models.CharField(max_length=100)
    item_type = models.CharField(max_length=20, choices=INVENTORY_TYPE_CHOICES, default='small')
    amount_small = models.PositiveIntegerField(default=0, verbose_name="Small Items Count")
    amount_large = models.PositiveIntegerField(default=0, verbose_name="Large Items Count")
    description = models.CharField(max_length=200, blank=True, null=True)
    
    class Meta:
        ordering = ['airway_bill', 'item_type']

    def __str__(self):
        return f"{self.airway_bill} - {self.get_item_type_display()} - S:{self.amount_small} L:{self.amount_large}"
    
    def total_items(self):
        return self.amount_small + self.amount_large