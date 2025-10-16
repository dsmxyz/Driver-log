from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.contrib import messages
from django.forms import formset_factory
from .models import DriverLog, TruckChecklist, TruckImage, ThermoKingImage, InventoryItem
from .forms import DriverLogForm, TruckChecklistForm, TruckImageForm, ThermoKingImageForm, CustomUserCreationForm, InventoryItemForm

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful!')
            return redirect('dashboard')
    else:
        form = CustomUserCreationForm()
    return render(request, 'logs/register.html', {'form': form})

def custom_logout(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')
    else:
        return redirect('logs/logout_confirm.html')

@login_required
def dashboard(request):
    logs = DriverLog.objects.filter(user=request.user).order_by('-created_at')[:5]
    return render(request, 'logs/dashboard.html', {'logs': logs})

@login_required
def log_list(request):
    logs = DriverLog.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'logs/log_list.html', {'logs': logs})

@login_required
def log_detail(request, pk):
    log = get_object_or_404(DriverLog, pk=pk, user=request.user)
    
    # Calculate inventory totals
    inventory_items = log.inventory_items.all()
    total_small = sum(item.amount_small for item in inventory_items)
    total_large = sum(item.amount_large for item in inventory_items)
    total_all = total_small + total_large
    
    context = {
        'log': log,
        'total_small': total_small,
        'total_large': total_large,
        'total_all': total_all,
    }
    
    return render(request, 'logs/log_detail.html', context)

@login_required
def log_create(request):
    TruckImageFormSet = formset_factory(TruckImageForm, extra=6, max_num=6)
    ThermoKingImageFormSet = formset_factory(ThermoKingImageForm, extra=3, max_num=3)
    InventoryFormSet = formset_factory(InventoryItemForm, extra=1, max_num=20, can_delete=True)
    
    if request.method == 'POST':
        log_form = DriverLogForm(request.POST)
        checklist_form = TruckChecklistForm(request.POST)
        truck_formset = TruckImageFormSet(request.POST, request.FILES, prefix='truck')
        thermoking_formset = ThermoKingImageFormSet(request.POST, request.FILES, prefix='thermoking')
        inventory_formset = InventoryFormSet(request.POST, prefix='inventory')
        
        if all([
            log_form.is_valid(),
            checklist_form.is_valid(),
            truck_formset.is_valid(),
            thermoking_formset.is_valid(),
            inventory_formset.is_valid()
        ]):
            log = log_form.save(commit=False)
            log.user = request.user
            log.save()
            
            checklist = checklist_form.save(commit=False)
            checklist.log = log
            checklist.save()
            
            # Save truck images
            for form in truck_formset:
                if form.cleaned_data.get('image'):
                    truck_image = form.save(commit=False)
                    truck_image.log = log
                    truck_image.save()
            
            # Save thermoking images
            for form in thermoking_formset:
                if form.cleaned_data.get('image'):
                    thermoking_image = form.save(commit=False)
                    thermoking_image.log = log
                    thermoking_image.save()
            
            # Save inventory items (skip empty forms and deleted forms)
            for form in inventory_formset:
                if (form.cleaned_data.get('airway_bill') and 
                    not form.cleaned_data.get('DELETE', False)):
                    inventory_item = form.save(commit=False)
                    inventory_item.log = log
                    inventory_item.save()
            
            messages.success(request, 'Driver log created successfully!')
            return redirect('log_detail', pk=log.pk)
    
    else:
        log_form = DriverLogForm()
        checklist_form = TruckChecklistForm()
        truck_formset = TruckImageFormSet(prefix='truck')
        thermoking_formset = ThermoKingImageFormSet(prefix='thermoking')
        inventory_formset = InventoryFormSet(prefix='inventory')
    
    context = {
        'log_form': log_form,
        'checklist_form': checklist_form,
        'truck_formset': truck_formset,
        'thermoking_formset': thermoking_formset,
        'inventory_formset': inventory_formset,
    }
    
    return render(request, 'logs/log_form.html', context)

@login_required
def log_update(request, pk):
    log = get_object_or_404(DriverLog, pk=pk, user=request.user)
    
    if request.method == 'POST':
        log_form = DriverLogForm(request.POST, instance=log)
        checklist_form = TruckChecklistForm(request.POST, instance=log.checklist)
        
        if all([
            log_form.is_valid(),
            checklist_form.is_valid()
        ]):
            log_form.save()
            checklist_form.save()
            messages.success(request, 'Driver log updated successfully!')
            return redirect('log_detail', pk=log.pk)
    
    else:
        log_form = DriverLogForm(instance=log)
        checklist_form = TruckChecklistForm(instance=log.checklist)
    
    context = {
        'log_form': log_form,
        'checklist_form': checklist_form,
        'is_update': True,
        'log': log,
    }
    
    return render(request, 'logs/log_form.html', context)