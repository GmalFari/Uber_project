from django.shortcuts import render, HttpResponse


def home(request):
    return render(request, 'user_master/index.html')
