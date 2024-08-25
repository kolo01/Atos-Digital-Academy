from django.urls import path
from .views import index
from .views import add
from .views import edit,fold

app_name = 'student'
urlpatterns = [
    
    path('', index, name='index'),
    path('add', add, name='add'),
    path('edit', edit, name='edit'),
    path('fold', fold, name='fold'),
    
]
