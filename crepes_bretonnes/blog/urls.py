from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('accueil', views.home, name="accueil"),
    path('articles', views.view_articles),
    path('boy', views.view_boy),
    path('redirection', views.view_redirection),
    path('date', views.date_act),
    path('addition/<int:nb1>/<int:nb2>/', views.addition),
    path('test', views.view_test),
    path('luck', views.view_luck),
]