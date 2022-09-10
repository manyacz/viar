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
            pass
            # messages.success(request, 'Форма заполнена!')
            return redirect('results')
        else:
            pass
            # messages.error(request, 'Форма не заполнена!')
    else:
        form = SearchForm()
    return render(request, 'rooms/search_room.html', {'form': form})

class Galery(ListView):
    model = Rooms
    template_name = 'rooms/galery.html'
    context_object_name = 'rooms'

    def get_queryset(self):
        return Rooms.objects.filter(photo=True)

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
   
    # def get_queryset(self):
    #     return Rooms.objects.filter(date_start__gte = date_in, date_end__lte = date_out)
    
    def search_from_form(request):
        if request.method == 'POST':
            form = SearchForm(request.POST)
            if form.is_valid():
                date_in = form.date_in
                date_out = form.date_out
                peoples = form.peoples
                if date_in and date_out and peoples:
                    messages.success(request, 'Мгновение и найдем варианты!')
                    return redirect('results')
                else:
                    messages.error(request, 'Ошибка заполнения поиска')
            else:
                messages.error(request, 'Ошибка регистрации')
        else:
            form = SearchForm()
        return render(request, 'rooms/results', {'form': form})
        
class RoomsAPIView(generics.ListAPIView):
    queryset = Rooms.objects.all()
    serializer_class = RoomsSerializer
    
