from django import template
register = template.Library()

@register.filter()
def class_on(mod):
    number = mod[1]
    state = "on"
    return state+number

@register.filter()
def class_off(mod):
    number = mod[1]
    state = "off"
    return state+number

@register.filter()
def src_on(mod):
    number = mod[1]
    src1 = "/static/img/on_"
    src2 = ".svg"
    return src1 + number + src2

@register.filter()
def src_off(mod):
    number = mod[1]
    src1 = "/static/img/off_"
    src2 = ".svg"
    return src1 + number + src2
