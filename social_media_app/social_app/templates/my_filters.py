from django import template

register = template.Library()

@register.filter(name='add_class')
def add_class(field, css_class):
    # This assumes 'field' is a Django form field object
    # If you're applying it to something else, this logic might need adjustment.
    return field.as_widget(attrs={"class": css_class})