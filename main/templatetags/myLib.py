from django import template
from django.conf import settings

register = template.Library()


@register.filter(is_safe=True)
def getattribute(obj, arg):
    try:
        obj = getattr(obj, str(arg.replace('()','')))
        if arg.find('()') != -1:
            return obj()
        else:
            if (obj):
                return obj
            else:
                return ''
    except:  
        settings.TEMPLATE_STRING_IF_INVALID  

@register.filter
def to_str(value):
    return str(value)