from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Room, Table, RoomBooking, TableBooking
from .forms import RoomBookingForm, TableBookingForm, RegisterForm
from .utils import is_room_available, is_table_available
from django.contrib.auth import login
from django.contrib.auth import logout


def logout_user(request):
    logout(request)
    return redirect('login')

def home(request):
    rooms = Room.objects.all()[:3]
    tables = Table.objects.all()[:3]
    return render(request, 'home.html', {'rooms':rooms,'tables':tables})

def room_list(request):
    rooms = Room.objects.all()
    return render(request, 'room_list.html', {'rooms':rooms})

def room_detail(request, pk):
    room = get_object_or_404(Room, pk=pk)
    form = RoomBookingForm()
    return render(request, 'room_detail.html', {'room':room,'form':form})

@login_required
def book_room(request, pk):
    room = get_object_or_404(Room, pk=pk)
    if request.method == 'POST':
        form = RoomBookingForm(request.POST)
        if form.is_valid():
            check_in = form.cleaned_data['check_in']
            check_out = form.cleaned_data['check_out']
            if not is_room_available(room, check_in, check_out):
                messages.error(request, 'Room not available for selected dates.')
                return redirect('room_detail', pk=pk)
            booking = form.save(commit=False)
            booking.user = request.user
            booking.room = room
            booking.save()
            messages.success(request, 'Room booked successfully.')
            return redirect('booking_success')
    else:
        form = RoomBookingForm()
    return render(request, 'room_detail.html', {'room':room,'form':form})

def table_list(request):
    tables = Table.objects.all()
    return render(request, 'table_list.html', {'tables':tables})

def table_detail(request, pk):
    table = get_object_or_404(Table, pk=pk)
    form = TableBookingForm()
    return render(request, 'table_detail.html', {'table':table,'form':form})

@login_required
def book_table(request, pk):
    table = get_object_or_404(Table, pk=pk)
    if request.method == 'POST':
        form = TableBookingForm(request.POST)
        if form.is_valid():
            date = form.cleaned_data['date']
            time = form.cleaned_data['time']
            end_time = form.cleaned_data['end_time']
            if not is_table_available(table, date, time, end_time):
                messages.error(request, 'Table slot not available.')
                return redirect('table_detail', pk=pk)
            booking = form.save(commit=False)
            booking.user = request.user
            booking.table = table
            booking.save()
            messages.success(request, 'Table booked successfully.')
            return redirect('booking_success')
    else:
        form = TableBookingForm()
    return render(request, 'table_detail.html', {'table':table,'form':form})

def booking_success(request):
    return render(request, 'booking_success.html')

@login_required
def my_bookings(request):
    rooms = RoomBooking.objects.filter(user=request.user)
    tables = TableBooking.objects.filter(user=request.user)
    return render(request, 'my_bookings.html', {'rooms':rooms,'tables':tables})

@login_required
def cancel_room_booking(request, pk):
    booking = get_object_or_404(RoomBooking, pk=pk, user=request.user)
    if request.method == 'POST':
        booking.status = 'Cancelled'
        booking.save()
        messages.success(request, 'Room booking cancelled.')
        return redirect('my_bookings')
    return render(request, 'confirm_cancel.html', {'booking':booking, 'type':'room'})

@login_required
def cancel_table_booking(request, pk):
    booking = get_object_or_404(TableBooking, pk=pk, user=request.user)
    if request.method == 'POST':
        booking.status = 'Cancelled'
        booking.save()
        messages.success(request, 'Table booking cancelled.')
        return redirect('my_bookings')
    return render(request, 'confirm_cancel.html', {'booking':booking, 'type':'table'})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Account created.')
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form':form})

def search(request):
    q = request.GET.get('q','')
    rooms = Room.objects.filter(name__icontains=q)
    tables = Table.objects.filter(table_number__icontains=q)
    return render(request, 'search_results.html', {'rooms':rooms,'tables':tables,'q':q})
