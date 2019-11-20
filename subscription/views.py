from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Subscription

def subscription(request):
    if request.method == 'POST':
        email = request.POST['email']

        # check if email is already subscribed
        has_subscribed = Subscription.objects.all().filter(email=email)
        if has_subscribed:
            messages.error(request, 'You have already made subscription. Thank you!')
            return redirect('/')
        subscribe = Subscription(email=email)
        subscribe.save()

        messages.success(request, 'Your subscription has been done successfuly, Thank you!')
        return redirect('/')
