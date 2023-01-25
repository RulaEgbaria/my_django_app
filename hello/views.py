from django.shortcuts import render
import mysql.connector
from django.utils import timezone
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


def check_sign_in(request):
   user_em = request.POST['emuser']

   user_p = request.POST['pw']
   flag = True
   conn = mysql.connector.connect(user='root', password='',
                                  host='localhost', database='users')


def questionnaire(request):
    return render(request, 'hello/questionnaire.html')


# def questionare_submit(request):
#     end_time = timezone.now()
#     time_spent = end_time - start_time
#     # Now you can save the time spent in your database
#     return redirect('/')


