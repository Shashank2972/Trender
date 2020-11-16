from django.shortcuts import render, HttpResponse ,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
# Create your views here.

def home(request):
    return render(request, 'account/signup.html')

def signup(request):
    if request.method=='POST':
        mail = request.POST.get('email','')
        username = request.POST.get('username','')
        name = request.POST.get('name','')
        password = request.POST.get('password','')
        conf_pass = request.POST.get('cpassword','')

        userCheck = User.objects.filter(username=username)
        if(userCheck):
            messages.error(request, 'Oops!! Username already taken')
            return redirect('/')

        if password==conf_pass:
            user_obj = User.objects.create_user(first_name =name, password = password, email= mail, username =username)
            user_obj.save()

    return redirect('/')

def user_login(request):
    if request.method=='POST':
        user_name=request.POST.get('username','')
        user_password=request.POST.get('password','')


    user = authenticate(username=user_name,password=user_password)
    if user is not None:
        login(request,user)
        messages.success(request, "Logged in")
        return redirect("/userpage")
    else:
        messages.error(request, "Invalid Username or Password")
        return redirect("/")

def user_logout(request):
    logout(request)
    messages.success(request, "Logged Out")
    return redirect("/")
