from django.shortcuts import render
from django.http import HttpResponse


def get_analytics(request):
    if request.method == "POST":
        return HttpResponse('request successful')
    else:
        return render(request, '404.html', {
            "content": "It looks like your trying your luck or your request is invalid or never existed.",
        })


def create_access_admin(request):
    if request.method == "POST":
        return HttpResponse('request successful')
    else:
        return render(request, '404.html', {
            "content": "It looks like your trying your luck or your request is invalid or never existed.",
        })
