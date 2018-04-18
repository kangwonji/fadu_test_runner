from django.http import JsonResponse

from utils import platform


def status(request):
    response = platform.info()
    return JsonResponse(response)
