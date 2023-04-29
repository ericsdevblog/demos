from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail

# Create your views here.


def send(request):
    send_mail(
        "Subject here",
        "Here is the message.",
        "from@example.com",
        ["huericnan@gmail.com"],
        fail_silently=False,
    )
    return HttpResponse("Email sent.")
