from django import template
register = template.Library()


@register.filter 
def addclass(field, css):
    return field.as_widget(attrs={'class': css})


@register.filter 
def addplaceholder(field, css):
    return field.as_widget(attrs={'placeholder': css, 'class': 'form-control'})

@register.filter
def str_to_list(x):
    return x[:-1].split('#')

@register.filter
def make_range(x):
    return range(x)

@register.simple_tag
def define(val=None):
  return val

@register.filter
def index(indexable, i):
    return indexable[i]

@register.filter
def str_to_list_length(x):
    return len(x[:-1].split('#'))