from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .forms import BookingForm

def index(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save()
            
            # Email Notification Logic
            subject = f"New Party Den Booking: {booking.name}"
            body = f"""
            New Booking Received!
            
            Name: {booking.name}
            Phone: {booking.phone}
            Date: {booking.event_date}
            Message: {booking.message}
            """
            
            try:
                send_mail(
                    subject,
                    body,
                    settings.EMAIL_HOST_USER,
                    ['your-receiving-email@gmail.com'], 
                    fail_silently=False,
                )
            except Exception as e:
                print(f"Email failed to send: {e}")

            return redirect('success')
    else:
        form = BookingForm()
    
    return render(request, 'index.html', {'form': form})

# THIS IS THE MISSING PIECE CAUSING THE ERROR
def success(request):
    return render(request, 'success.html')

