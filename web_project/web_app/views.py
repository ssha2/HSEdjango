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
    try:
        survey = Survey(request.POST)
        #survey.changed_data[""]

        return HttpResponse('{ "capt":"Результат","text":"Данные успешно получены" }')
    except Exception as e:
        #return HttpResponse(status=500,text=str(e))
        return HttpResponse('{ "capt":"Ошибка","text":"'+str(e)+'" }')
  