from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
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

# users/<id>
def user_detail_view(request, id):
    try:
        user = get_object_or_404(User, id=id)
    except User.DoesNotExist:
        raise Http404("User does not exist.")
    else:
        return render(request, 'user_detail.html', {'user': user})