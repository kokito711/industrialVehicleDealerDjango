# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_http_methods

from .service import usermanagement


@require_http_methods(["GET", "POST"])
def index(request):
    if request.method == "GET":
        return JsonResponse(data=usermanagement.get_all_users(), safe=False)
    else:
        return JsonResponse(data=usermanagement.create_new_user(request.body))


@require_http_methods(["GET", "PUT"])
def selected_user(request):
    return HttpResponse("Hello, world. You're at the users index.")
