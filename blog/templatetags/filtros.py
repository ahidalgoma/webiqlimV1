from django import template


register = template.Library()

@register.filter(name='check')
def check(id):
    try: return "?pagina_%d" % id
    except KeyError: return ""