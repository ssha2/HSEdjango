from django.shortcuts import render
from django.http import HttpResponse,HttpRequest

from .survey import Survey

def index(request):
    return render(request, "index.html")


def catalog(request):
     return render(request, "catalog.html")

def podcats(request):
     return render(request, "podcats.html")


def articles(request):
    return render(request, "articles.html")

def surv(request):
    return render(request, "surv.html")


def calc(request):
    return render(request, "calc.html")

def surv_result(request):

    survey = Survey(request.POST)
    # if is_ajax:
    #     if request.method == 'GET':
    #         todos = list(Todo.objects.all().values())
    #         return JsonResponse({'context': todos})
    #     return JsonResponse({'status': 'Invalid request'}, status=400)
    # else:
    #     return HttpResponseBadRequest('Invalid request')
    return HttpResponse(survey.frequency)