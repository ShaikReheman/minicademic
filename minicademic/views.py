from django.http import HttpResponse, HttpResponseNotAllowed


def update_repository(request):
    return HttpResponse('Web server updated!')