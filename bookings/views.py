from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import BookingForm
from .models import Booking


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created! You can now log in.")
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required
def account(request):
    return render(request, 'account.html', {'user': request.user})

@login_required
def history(request):
    # Fetch only the logged-in user's bookings
    user_bookings = Booking.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'history.html', {'bookings': user_bookings})

def contact(request):
    return render(request, 'contact.html')

def index(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            if request.user.is_authenticated:
                booking.user = request.user
            booking.save()
            return redirect('success')
    else:
        form = BookingForm()
    return render(request, 'index.html', {'form': form})

def success(request):
    return render(request, 'success.html')