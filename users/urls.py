from django.urls import path
from users import views

app_name = "users"

urlpatterns = [
    path("register/",views.UserRegister.as_view(),name="register-user"),
    path("login/",views.UserLoginView.as_view(),name="login-user"),

]