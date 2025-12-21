from django.db import models
from django.contrib.auth.models import User

STATUS_CHOICES = (
    ('Booked', 'Booked'),
    ('Cancelled', 'Cancelled'),
    ('Completed', 'Completed'),
)

class Room(models.Model):
    ROOM_TYPES = (('Single','Single'),('Double','Double'),('Deluxe','Deluxe'),('Suite','Suite'))
    name = models.CharField(max_length=120)
    room_type = models.CharField(max_length=30, choices=ROOM_TYPES)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    capacity = models.IntegerField()
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='rooms/', blank=True, null=True)
    def __str__(self): return self.name

class Table(models.Model):
    table_number = models.CharField(max_length=20)
    capacity = models.IntegerField()
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='tables/', blank=True, null=True)
    def __str__(self): return f"Table {self.table_number}"

class RoomBooking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Booked')
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self): return f"{self.user.username} - {self.room.name}"

class TableBooking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    end_time = models.TimeField(null=True, blank=True)
    guests = models.IntegerField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Booked')
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self): return f"{self.user.username} - Table {self.table.table_number}"
