from django.conf import settings

def is_debug_mode(context):
	return {"is_debug_mode": settings.DEBUG}
