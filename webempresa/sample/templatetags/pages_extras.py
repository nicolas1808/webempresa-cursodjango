from django import template
from sample.models import Page

register = template.Library()

@register.simple_tag
def get_page_list():
    sample = Page.objects.all()
    return sample

# Se utiliza para las paginas de politica de privacicadad, cookies