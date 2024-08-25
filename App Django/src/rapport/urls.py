from django.urls import path
from .views import index
# from .views import add
# from .views import edit

app_name = 'rapport'
urlpatterns = [
    
    path('', index, name='index'),
    # path('add', add),
    # path('edit', edit),
    
]
