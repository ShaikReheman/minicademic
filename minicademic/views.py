from django.http import HttpResponse, HttpResponseNotAllowed


def update_repository():
    return HttpResponse('Web server updated!')