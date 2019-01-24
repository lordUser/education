from django import template


register = template.Library()


@register.simple_tag()
def admin_chenge(obj):
    return reverse("admin:{}_{}_change".format(obj._meta.app_label, obj._meta.model_name), args=(obj.id,))
