from django.contrib import admin
from django.urls import path
from .views import *



urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('rooms/', HomeRooms.as_view(), name='rooms'),
    path('about/', about, name='about'),
    path('prices/', prices, name='prices'),
    path('galery/', galery, name='galery'),
    path('api/v1/roomslist/', RoomsAPIView.as_view()),
    
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('search_room/', search_room, name='search_room'),
    path('results/', search_from_form, name='results'),
    path('rooms/<int:pk>/', ViewRooms.as_view(), name='view_rooms'),
]

