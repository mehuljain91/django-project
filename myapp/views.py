from django.shortcuts import render
from django.http import HttpResponse
from .models import User

# Create your views here.

def hello_view(request):
    return HttpResponse("Hello, World!")


# users list
def users_view(request):
    users = User.objects.all()
    return render(request, 'users.html', {'users': users})