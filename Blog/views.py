from django.shortcuts import render, get_object_or_404
from .models import *
# Create your views here.


def Home(request):
    posts = Post.objects.filter(estado=True)
    return render(request,'blog/index.html',{'posts':posts})


def Generales(request):
    posts = Post.objects.filter(estado=True, categoria=Categoria.objects.get(nombre__iexact  = 'Generales'))
    return render(request,'blog/generales.html',{'posts': posts})


def Programacion(request):
    posts = Post.objects.filter(estado=True, categoria=Categoria.objects.get(nombre__iexact ='Programacion'))
    return render(request,'blog/programacion.html',{'posts':posts})


def Video_Juegos(request):
    posts = Post.objects.filter(estado=True, categoria=Categoria.objects.get(nombre__iexact ='Video Juegos'))
    return render(request,'blog/video_juegos.html',{'posts':posts})


def Tutoriales(request):
    posts = Post.objects.filter(estado=True, categoria=Categoria.objects.get(nombre__iexact ='Tutoriales'))
    return render(request,'blog/tutoriales.html',{'posts':posts})


def Tecnologia(request):
    posts = Post.objects.filter(estado=True, categoria=Categoria.objects.get(nombre__iexact = 'Tecnologia'))
    return render(request,'blog/tecnologia.html',{'posts':posts})

def detallePost(request,slug):
    post = get_object_or_404(Post,slug=slug)
    return render(request,'blog/post.html',{'posts_detalle':post})

