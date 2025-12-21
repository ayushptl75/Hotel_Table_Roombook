from django.contrib import admin
from .models import Room, Table, RoomBooking, TableBooking
import csv
from django.http import HttpResponse

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('name','room_type','price','capacity')

@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ('table_number','capacity')

@admin.register(RoomBooking)
class RoomBookingAdmin(admin.ModelAdmin):
    list_display = ('user','room','check_in','check_out','status','created_at')
    list_filter = ('status','room')
    actions = ['export_as_csv']
    def export_as_csv(self, request, queryset):
        field_names = ['user','room','check_in','check_out','status','created_at']
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=room_bookings.csv'
        writer = csv.writer(response)
        writer.writerow(field_names)
        for obj in queryset:
            writer.writerow([obj.user.username, obj.room.name, obj.check_in, obj.check_out, obj.status, obj.created_at])
        return response

@admin.register(TableBooking)
class TableBookingAdmin(admin.ModelAdmin):
    list_display = ('user','table','date','time','end_time','status','created_at')
    list_filter = ('status','table')
