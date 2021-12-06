from django.urls import path
from .views import Home,Generales,Tecnologia,Programacion,Video_Juegos,Tutoriales,detallePost

urlpatterns = [

    path('',Home,name='index'),
    path('generales/',Generales,name='generales'),
    path('tutoriales/',Tutoriales,name='tutoriales'),
    path('tecnologia/',Tecnologia,name='tecnologia'),
    path('pogramacion/',Programacion,name='programacion'),
    path('Video_Juegos/',Video_Juegos,name='Video_Juegos'),
    path('<slug:slug>/',detallePost,name='detalle'),
]