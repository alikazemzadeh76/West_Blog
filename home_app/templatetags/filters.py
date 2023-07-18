from django import template


register = template.Library()

@register.filter
def max_width(value, arg):
    return value[:35] + ' ...'