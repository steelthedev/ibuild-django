from django.urls import path,include
from . import views


app_name = "accounts"

urlpatterns = [
    path('login',views.Signin, name="login"),
    path('signup', views.SignUp, name="signup"),
    path('logout',views.Logout_view, name="logout"),
]


