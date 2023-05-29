from django.urls import path


from core.views import SignupView, LoginView, ProfileView, UpdatePasswordView

urlpatterns = [
    path("signup", SignupView.as_view()),
    path("login", LoginView.as_view()),
    path("profile", ProfileView.as_view()),
    path("update_password", UpdatePasswordView.as_view()),
]