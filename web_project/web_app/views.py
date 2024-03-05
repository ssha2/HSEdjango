import logging

from django.shortcuts import render
from django.http import HttpResponse,HttpRequest

from .survey import Survey

logger = logging.getLogger('django')

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

def mystuds(request):
   
   elem_me = {
        'name': 'Смирнов Даниил',
        'foto_path': 'static/photos/arni.png',
        'email': 'smitnv@example.com',
        'phone': ''
    }
   elem_dir = {
        'name': 'Смирнов Даниил',
        'foto_path': 'static/photos/arni.png',
        'email': 'smitnv@example.com',
        'phone': ''
    }
   elem_men = {
        'name': 'Смирнов Даниил',
        'foto_path': 'static/photos/arni.png',
        'email': 'smitnv@example.com',
        'phone': ''
    }
   elem_st1 = {
        'name': 'Смирнов Даниил',
        'foto_path': 'static/photos/arni.png',
        'email': 'smitnv@example.com',
        'phone': ''
    }
   elem_st2 = {
        'name': 'Смирнов Даниил',
        'foto_path': 'static/photos/arni.png',
        'email': 'smitnv@example.com',
        'phone': ''
    }
   
   data_people ={
       'me':{
           'label':'О себе',
           'details':elem_me
       },
       'direct':{
           'label':'Руководитель',
           'details':elem_me
       },
       'manager':{
           'label':'Mенеджер',
           'details':elem_me
       },
       'st1':{
           'label':'Cтудент 1',
           'details':elem_me
       },
       'st2':{
           'label':'Cтудент 2',
           'details':elem_me
       },

   }  
   descript = {
        'prod_name': 'Душить питона',
        'prod_desctipr': 'Душить питона'
    }


   return render(request, "mystuds.html",{'descript':descript,'data': data_people})


def surv_result(request):
    try:
        survey = Survey(request.POST)
        #survey.changed_data[""]
   
        return HttpResponse('{ "capt":"Результат from server","text":"Данные успешно получены для'+survey.data['email']+'" }')
    except Exception as e:
        #return HttpResponse(status=500,text=str(e))
        return HttpResponse('{ "capt":"Ошибка","text":"'+str(e)+'" }')
  