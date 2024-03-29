from django import template
from urllib.parse import unquote, quote
register = template.Library()


@register.filter 
def addclass(field, css):
    return field.as_widget(attrs={'class': css, 'class': 'form-control shadow-none'})

@register.filter 
def addvalue(field, css):
    return field.as_widget(attrs={'value': css, 'class': 'form-control shadow-none'})

@register.filter 
def addwidth(field):
    return field.as_widget(attrs={'style': 'width: 170px;', 'class': 'rounded'})

@register.filter 
def addplaceholder(field, css):
    return field.as_widget(attrs={'placeholder': css, 'class': 'form-control shadow-none'})

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

@register.filter
def code(x):
    x = str(x)
    return quote(x)

@register.filter
def decode(x):
    x = str(x)
    return unquote(x)

@register.filter
def to_str(x):
    return str(x)

@register.filter
def to_int(x):
    return int(x)

@register.filter 
def addchecked(field, css):
    return field.as_widget(attrs={'checked': css})