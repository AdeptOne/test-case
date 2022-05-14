from django import template


register = template.Library()


@register.filter()
def get_short_link(request, short_code):
    return request.build_absolute_uri('/') + short_code
