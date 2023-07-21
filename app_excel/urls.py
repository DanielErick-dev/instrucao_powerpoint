from django.urls import path
from .views import index, topico1, topico2, topico3, topico4, topico5,\
    topico6, topico7, topico8, topico9, topico10, topico11, topico12,\
    topico13, topico14, topico15, topico16, topico17, topico18, topico19, topico20

app_name = 'app_excel'
urlpatterns = [
    path('', index, name='index'),
    path('topico1', topico1, name='topico1'),
    path('topico2', topico2, name='topico2'),
    path('topico3', topico3, name='topico3'),
    path('topico4', topico4, name='topico4'),
    path('topico5', topico5, name='topico5'),
    path('topico6', topico6, name='topico6'),
    path('topico7', topico7, name='topico7'),
    path('topico8', topico8, name='topico8'),
    path('topico9', topico9, name='topico9'),
    path('topico10', topico10, name='topico10'),
    path('topico11', topico11, name='topico11'),
    path('topico12', topico12, name='topico12'),
    path('topico13', topico13, name='topico13'),
    path('topico14', topico14, name='topico14'),
    path('topico15', topico15, name='topico15'),
    path('topico16', topico16, name='topico16'),
    path('topico17', topico17, name='topico17'),
    path('topico18', topico18, name='topico18'),
    path('topico19', topico19, name='topico19'),
    path('topico20', topico20, name='topico20')


]


