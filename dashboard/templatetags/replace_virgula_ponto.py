from django import template
register = template.Library()

@register.simple_tag
def replace_virgula_ponto(value):
    value = str(value)
    return value.replace(',','.')
