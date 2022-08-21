# Create your views here.
from django.http import JsonResponse, HttpResponseNotAllowed
from django.views.decorators.http import require_http_methods

from .service import usermanagement


@require_http_methods(["GET", "POST"])
def index(request):
    if request.method == "GET":
        return JsonResponse(data=usermanagement.get_all_users(), safe=False)
    else:
        body = request.body
        user = usermanagement.get_user(body)
        if user is not None:
            return JsonResponse(data=user, status=200)
        return JsonResponse(data=usermanagement.create_new_user(body), status=201)


@require_http_methods(["GET", "PUT"])
def selected_user(request, user_code):
    if request.method == "GET":
        get_user_by_id = usermanagement.get_user_by_id(user_code)
        if get_user_by_id is not None:
            return JsonResponse(data=get_user_by_id)
        else:
            return JsonResponse(data={"message": "user not found"}, content_type="application/json", status=404)
    else:
        return HttpResponseNotAllowed()


@require_http_methods(["POST"])
def auth(request):
    body = request.body
    auth_user = usermanagement.get_user_by_id(body['client_id'])
    if auth_user is not None:
        return JsonResponse(data=auth_user)
    return JsonResponse(data={"message": "Unauthorized"}, status=401)
