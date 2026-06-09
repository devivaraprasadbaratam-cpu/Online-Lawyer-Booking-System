from django import template

register = template.Library()

@register.filter
def star_range(value):
    try:
        # Convert value to integer
        value = int(value)
        return range(value)
    except ValueError:
        return range(0)

