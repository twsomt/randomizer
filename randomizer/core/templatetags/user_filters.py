from django import template
register = template.Library()


@register.filter 
def addclass(field, css):
    return field.as_widget(attrs={'class': css})


@register.filter 
def addplaceholder(field, css):
    return field.as_widget(attrs={'placeholder': css, 'class': 'form-control'})


@register.filter
def str_to_list(field):
    return field.split(';')