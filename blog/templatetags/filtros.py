from django import template


register = template.Library()

@register.filter(name='check')
def check(id):
    try: 
        if id>100:
            return "pagina_%d" % id
        else:
            if id>10:
                return "pagina_0%d" % id
            else:
                return "pagina_00%d" % id
    except KeyError: return ""