from .models import RoomBooking, TableBooking

def is_room_available(room, check_in, check_out):
    qs = RoomBooking.objects.filter(room=room, status='Booked')
    for b in qs:
        if (b.check_in < check_out) and (b.check_out > check_in):
            return False
    return True

def is_table_available(table, date, start_time, end_time):
    qs = TableBooking.objects.filter(table=table, date=date, status='Booked')
    for b in qs:
        if (b.time < end_time) and (b.end_time > start_time):
            return False
    return True
