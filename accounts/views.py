from django.db.models.fields import EmailField
from django.shortcuts import redirect, render
from accounts.models import *
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.contrib.auth import login , logout , authenticate


def SignUp(request):

    if request.method == "POST":
        
        first_name = request.POST['f_name']
        last_name = request.POST['l_name']
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password != password2:
            messages.info(request, "Password Must Be The Same")
            return redirect('accounts:signup')
        elif User.objects.filter(username = username):
            messages.info(request, "User Exists")
            return redirect('accounts:signup')
        elif "@" not in username:
            messages.info(request, "Please Enter A Valid Email Address")
            return redirect('accounts:signup')
        elif len(first_name) < 1:
            messages.info(request, "First Name Cannot Lesser Than One Character")
            return redirect('accounts:signup')
        elif len(last_name) < 1:
            messages.info(request, "Last Name Cannot Be Lesser Than One Character")
            return redirect('accounts:signup')
        else:
            hashedpwd = make_password(password)
            user = User.objects.create(username = username , password = hashedpwd , last_name = last_name , first_name = first_name , email = username)
            user.save()
            user.refresh_from_db()
            user_profile = Profile.objects.get(user = user)
            user_profile.first_name = user_profile.user.first_name
            user_profile.last_name = user_profile.user.last_name
            user_profile.email = user_profile.user.email
            user_profile.save()

            messages.info(request, "You have been registered successfully now proceed to login")
            return redirect('accounts:login')
     

    return render(request, 'accounts/signup.html')



def Signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        
        if User.objects.filter(username=username):
            user = authenticate(request,username = username , password = password)

            if user is not None:
                login(request, user)
                return redirect("dashboard:dashboard")

            else:
                messages.info(request, "Incorrect Details" )
                return redirect("accounts:login")

        else:
            messages.info(request, "This User Does Not Exist" )
            return redirect("accounts:login")
    return render(request, 'accounts/login.html')



def Logout_view(request):

    logout(request)

    messages.info(request, "Thank You , You Have Logged Out Successfully" )
    return redirect("accounts:login")


