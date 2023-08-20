# custom_filters.py
from django import template

register = template.Library()

@register.filter
def dict_lookup(dictionary, key):
    key = key.lower()
    return dictionary.get(key)
