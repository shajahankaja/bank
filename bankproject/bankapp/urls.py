from django.urls import path
from . import views

app_name='bankapp'

urlpatterns = [
    path('',views.index,name='index'),
    path('login/', views.login, name='login'),
    path('signup/',views.signup,name='signup'),
    path('newpage/',views.newpage,name='newpage'),
    path('form/',views.form,name='form'),
    path('confirmpage/',views.confirmpage,name='confirmpage'),
    path('about/',views.about,name='about'),
]