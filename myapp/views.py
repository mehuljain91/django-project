from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User

# Create your views here.

def hello_view(request):
    return HttpResponse("Hello, World!")


# users list
def users_view(request):
    users = User.objects.all()
    return render(request, 'users.html', {'users': users})

# create new_user
def new_user_view(request):
    if request.method == 'POST':
        
        name = request.POST['name']
        email = request.POST['email']
        role = request.POST['role']

        user = User(name=name, email=email, role=role)
        user.save()

        return redirect('users')

    return render(request, 'new_user.html')