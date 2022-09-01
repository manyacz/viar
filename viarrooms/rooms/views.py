from .models import Rooms
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView
from .forms import RoomsForm, UserRegisterForm, UserLoginForm, ContactForm, SearchForm
from django.contrib import messages
from django.contrib.auth import login, logout
from django.core.mail import send_mail
from rest_framework import generics
from .serialazers import RoomsSerializer

def home(request):
    return render(request, template_name='rooms/home.html')
    
def about(request):
    return render(request, template_name='rooms/about.html')

def prices(request):
    return render(request, template_name='rooms/prices.html')

def galery(request):
    return render(request, template_name='rooms/galery.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            messages.success(request, 'Вы успешно заригистрировались')
            return redirect('home')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = UserRegisterForm()
    return render(request, 'rooms/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data = request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm()
    return render(request, 'rooms/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')

def search_room(request):
    if request.method == 'POST':
        form = SearchForm(data = request.POST)
        if form.is_valid():
            messages.success(request, 'Форма заполнена!')
            return redirect('results')
        else:
            messages.error(request, 'Форма не заполнена!')
    else:
        form = SearchForm()
    return render(request, 'rooms/search_room.html', {'form': form})

class HomeRooms(ListView):
    model = Rooms
    template_name = 'rooms/home_rooms_list.html'
    context_object_name = 'rooms'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Комнаты'
        return context
    
    def get_queryset(self):
        return Rooms.objects.filter(is_published=True)

class ViewRooms(DetailView):
    model = Rooms
    context_object_name = 'rooms_item'

class CreateRooms(CreateView):
    form_class = RoomsForm
    template_name = 'rooms/add_rooms.html'
    
class RoomsBySearch(ListView):
    model = Rooms
    template_name = 'rooms/home_rooms_list.html'
    context_object_name = 'rooms'
    allow_empty = False
    
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Rooms.objects.get(pk=self.kwargs['title'])
        return context
    
    def get_queryset(self):
        return Rooms.objects.filter()
        

class RoomsAPIView(generics.ListAPIView):
    queryset = Rooms.objects.all()
    serializer_class = RoomsSerializer
    
# def test(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             mail = send_mail(form.cleaned_data['subject'], form.cleaned_data['content'], 'mynewtestlogdj@gmail.com', ['nelubimayaya@gmail.com'], fail_silently=False)
#             if mail:
#                 messages.success(request, 'Письмо отправлено!')
#                 return redirect('test')
#             else:
#                 messages.error(request, 'Ошибка отправки')
#         else:
#             messages.error(request, 'Ошибка регистрации')
#     else:
#         form = ContactForm()
#     return render(request, 'rooms/test.html', {'form': form})