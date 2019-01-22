from django.conf import settings
from django.template.context_processors import request


def core(request):
	return settings.__dict__['_wrapped'].__dict__
