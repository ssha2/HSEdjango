import logging

from django.shortcuts import render
from django.http import HttpResponse,HttpRequest
from django.db.models import Avg, Min,Max,Sum
from django.contrib.auth.decorators import login_required

from .models import Surmodel,Catalog


logger = logging.getLogger('django')

def index(request):
    return render(request, "index.html")


def catalog(request):
     catalog = Catalog.objects.filter(id__gte=0) #id>0
     return render(request, "catalog.html",{'data': catalog})

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



def task1002(request):
    try:
        param1 = float(request.GET.get('float', None))
        results="[положительное]" if param1>0 else ("[отрицательное]" if param1<0 else "[нулевое]")
        return HttpResponse('{ "capt":"Результат from server","text":"Данные успешно получены для ['+str(param1)+'] это число ' +results+'" }')
    except Exception as e:
        #return HttpResponse(status=500,text=str(e))
        return HttpResponse('{ "capt":"Ошибка","text":"'+str(e)+'" }')
    

@login_required(login_url='accounts/login/')
def stats(request):

    # if not  ( request.user.username=="analist" and request.user.is_authenticated):
    #     return HttpResponse("Пожалуйста, авторизуйтесь.")

    survey_filtered = Surmodel.objects.filter(id__gte=0) #id>0
    if request.GET.get('age_value'):
        if (request.GET.get('age_case')=="eq"): #=
            survey_filtered=survey_filtered.filter(age=request.GET.get('age_value'))
        elif (request.GET.get('age_case')=="lt"):  #<
            survey_filtered=survey_filtered.filter(age__lt=request.GET.get('age_value')) 
        elif (request.GET.get('age_case')=="gt"):  #>
            survey_filtered=survey_filtered.filter(age__gt=request.GET.get('age_value'))  
        elif (request.GET.get('age_case')=="lte"):  #=<
            survey_filtered=survey_filtered.filter(age__lte=request.GET.get('age_value')) 
        elif (request.GET.get('age_case')=="gte"):  #>=
            survey_filtered=survey_filtered.filter(age__gte=request.GET.get('age_value'))        

    if request.GET.get('sex'):
        if not request.GET.get('sex')=="any":
            survey_filtered=survey_filtered.filter(sex=request.GET.get('sex'))
    
    if request.GET.get('partday'):
        if not request.GET.get('partday')=="any":
            survey_filtered=survey_filtered.filter(partday=request.GET.get('partday'))

    if request.GET.get('sort_value'):
        if request.GET.get('sort_case')=="asc": #" asc> column"
            survey_filtered=survey_filtered.order_by(request.GET.get('sort_value'))
        else : # desc> -column
            survey_filtered=survey_filtered.order_by("-"+request.GET.get('sort_value'))

    calc = {
        #                                             field   field__avg
        'avg_age':round(survey_filtered.aggregate(Avg("age"))['age__avg'],0),
        'count_rec':survey_filtered.count()
    }

    return render(request, "stats.html",{'data':survey_filtered,'calc':calc})


def surv_result(request):
    try:
        # 1002
        try:
            task1002=float(request.POST["age"])
        except ValueError:
            raise Exception("Возраст должен быть числом")
        if not task1002.is_integer():
            raise Exception("Возраст должен быть целым числом")
        if task1002<=0:
            raise Exception("Возраст должен быть положительным числом >0")
        if task1002<18:
            raise Exception("Вам должно быть 18")
        #save db
        survey = Surmodel.objects.create( \
            frequency=  request.POST["frequency"] if "frequency" in request.POST else "", \
            partday=request.POST["partday"] if "partday" in request.POST else "", \
            prefsport=request.POST["prefsport"] if "prefsport" in request.POST else "", \
            consume=request.POST["consume"] if "consume" in request.POST else "", \
            prodtype=request.POST["prodtype"] if "prodtype" in request.POST else "", \
            bodytype=request.POST["bodytype"] if "bodytype" in request.POST else "", \
            sex=request.POST["sex"] if "sex" in request.POST else "", \
            age=task1002, \
            email=request.POST["email"] if "email" in request.POST else "", \
            comment=request.POST["comment"] if "comment" in request.POST else "" \
        )     
        survey.save()
        text='{ "capt":"Ответ сервера","text":"Данные успешно получены и сохранены id='+str(survey.id)+'" }'
        return HttpResponse(text)
    except Exception as e:
        #return HttpResponse(status=500,text=str(e))
        return HttpResponse('{ "capt":"Ошибка сервера","text":"'+str(e)+'" }')
  