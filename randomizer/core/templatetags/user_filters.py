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
    x =  field.split('/////')
    x = [i.split(", '") for i in x]

    for i in x:
        for j in range(len(i)):
            if j == 0:
                i[j] = ''.join([h for h in i[j] if h.isdigit()])
            elif j == 1:
                i[j] = i[j][12:-1]
            elif j == 2:
                i[j] = i[j][14:-1]
            elif j == 3:
                i[j] = i[j][13:-1]
            else:
                break
    return x

@register.filter
def id(field):
    return field[0]

@register.filter
def link(field):
    return ''.join(field[1:2])

@register.filter
def first_name(field):
    return ''.join(field[2:3])

@register.filter
def last_name(field):
    return ''.join(field[3:4])

