from django.urls import path
from .views import index, topico1, topico2, topico3, topico4, topico5, topico6

app_name = 'app_excel'
urlpatterns = [
    path('', index, name='index'),
    path('topico1', topico1, name='topico1'),
    path('topico2', topico2, name='topico2'),
    path('topico3', topico3, name='topico3'),
    path('topico4', topico4, name='topico4'),
    path('topico5', topico5, name='topico5'),
    path('topico6', topico6, name='topico6')
]
