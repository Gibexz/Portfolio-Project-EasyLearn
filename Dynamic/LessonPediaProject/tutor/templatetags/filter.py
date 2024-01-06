# Create a templatetags directory in your app

from django import template

register = template.Library()

@register.filter(name='increment')
def increment(value):
    return value + 1
