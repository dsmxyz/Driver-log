from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import DriverLog, TruckChecklist, TruckImage, ThermoKingImage, InventoryItem

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class DriverLogForm(forms.ModelForm):
    class Meta:
        model = DriverLog
        fields = [
            'start_datetime', 'end_datetime', 'work_description', 'truck',
            'truck_mileage', 'truck_fuel_level', 'def_level', 'thermoking_hours',
            'error_lights_faults'
        ]
        widgets = {
            'start_datetime': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'end_datetime': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'work_description': forms.Textarea(attrs={'rows': 4}),
            'error_lights_faults': forms.Textarea(attrs={'rows': 3}),
        }

class TruckChecklistForm(forms.ModelForm):
    class Meta:
        model = TruckChecklist
        fields = [
            'lights', 'mirrors', 'tires', 'brakes', 'suspension_check',
            'pallet_jack', 'shrink_wrap', 'pallets', 'def_fluid', 'notes'
        ]
        widgets = {
            'notes': forms.Textarea(attrs={'rows': 3}),
        }

class TruckImageForm(forms.ModelForm):
    class Meta:
        model = TruckImage
        fields = ['image_type', 'image']

class ThermoKingImageForm(forms.ModelForm):
    class Meta:
        model = ThermoKingImage
        fields = ['image_type', 'image']

class InventoryItemForm(forms.ModelForm):
    class Meta:
        model = InventoryItem
        fields = ['airway_bill', 'item_type', 'amount_small', 'amount_large', 'description']
        widgets = {
            'description': forms.TextInput(attrs={'placeholder': 'Optional item description'}),
            'amount_small': forms.NumberInput(attrs={'min': '0', 'class': 'form-control'}),
            'amount_large': forms.NumberInput(attrs={'min': '0', 'class': 'form-control'}),
        }
    
    def clean(self):
        cleaned_data = super().clean()
        amount_small = cleaned_data.get('amount_small', 0)
        amount_large = cleaned_data.get('amount_large', 0)
        
        # Ensure at least one item is entered if airway bill is provided
        airway_bill = cleaned_data.get('airway_bill')
        if airway_bill and amount_small == 0 and amount_large == 0:
            raise forms.ValidationError("Please enter at least one item count (small or large) if airway bill is provided.")
        
        return cleaned_data