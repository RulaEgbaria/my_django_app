from django.shortcuts import render
import models
# Create your views here.
def index(request):
    return render(request, 'hello/index.html')

def login_user(request):
    return render(request, 'hello/login_user.html')

def visitor(request):
    return render(request, 'hello/visitor.html')

def sign_in(request):
    return render(request, 'hello/sign_in.html')

def sign_up(request):
    return render(request, 'hello/sign_up.html')



