from django.urls import path
from .views import index
from .views import add
from .views import edit


app_name = 'users'
urlpatterns = [
    
    path('', index, name='index'),
    path('add', add, name='add'),
    path('edit', edit, name='edit'),
    
]
