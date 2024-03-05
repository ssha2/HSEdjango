from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("catalog", views.catalog, name="catalog"),
    path("podcats", views.podcats, name="podcats"),
    path("articles", views.articles, name="articles"),
    path("surv", views.surv, name="surv"),
    path("calc", views.calc, name="calc"),
    path("mystuds", views.mystuds, name="mystuds"),
    
    path("surv_result", views.surv_result, name="surv_result"),
    
]



