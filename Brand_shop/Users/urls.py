from django.urls import path
from Users.views import Register


urlpatterns = [
    path('register/',  Register.as_view()),
]

