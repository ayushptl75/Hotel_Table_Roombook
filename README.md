# Hotel Reservation (Django) - Minimal Starter

This is a minimal, ready-to-run Django project scaffold for a Hotel Table & Room Reservation System.
It includes:
- Django app `bookings`
- Models for Room, Table, RoomBooking, TableBooking
- Views, URLs, templates for listing, booking, availability, search, cancel, authentication (signup/login)
- Admin registrations and CSV export actions
- Email utility (configure SMTP in settings)
- Bootstrap-based templates and a homepage carousel

## Quick start

1. Create and activate a Python virtualenv.
2. Install requirements:
   ```
   pip install -r requirements.txt
   ```
3. Run migrations:
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```
4. Create a superuser:
   ```
   python manage.py createsuperuser
   ```
5. Run server:
   ```
   python manage.py runserver
   ```

## Notes
- Add `MEDIA_ROOT` and `STATICFILES` as needed.
- Configure SMTP settings in `hotel_reservation/settings.py` for real email sending.
- This scaffold is simplified for educational use. For production, follow Django deployment best practices.
