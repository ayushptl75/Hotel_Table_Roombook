from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
   
]

urlpatterns = [
    path('', views.home, name='home'),
    path('rooms/', views.room_list, name='room_list'),
    path('rooms/<int:pk>/', views.room_detail, name='room_detail'),
    path('rooms/<int:pk>/book/', views.book_room, name='book_room'),
    path('tables/', views.table_list, name='table_list'),
    path('tables/<int:pk>/', views.table_detail, name='table_detail'),
    path('tables/<int:pk>/book/', views.book_table, name='book_table'),
    path('success/', views.booking_success, name='booking_success'),
    path('my-bookings/', views.my_bookings, name='my_bookings'),
    path('rooms/<int:pk>/availability/', views.room_detail, name='room_availability'),
    path('tables/<int:pk>/availability/', views.table_detail, name='table_availability'),
    path('room-booking/<int:pk>/cancel/', views.cancel_room_booking, name='cancel_room_booking'),
    path('table-booking/<int:pk>/cancel/', views.cancel_table_booking, name='cancel_table_booking'),
    path('register/', views.register, name='register'),
    path('search/', views.search, name='search'),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='/login/'), name='logout'),
]
