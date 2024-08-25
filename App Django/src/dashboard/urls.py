from django.urls import path
from .views import index,login

app_name = 'dashboard'
urlpatterns = [
    
    path('home/', index, name='index'),
    path('', login, name='login')
]
