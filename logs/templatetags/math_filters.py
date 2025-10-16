from django import template

register = template.Library()

@register.filter
def sum_attr(queryset, attr):
    return sum(getattr(item, attr, 0) for item in queryset)

@register.filter
def total_items(inventory_item):
    return inventory_item.amount_small + inventory_item.amount_large