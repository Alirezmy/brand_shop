from django.urls import path
from Products.views import ProductGenericsView


urlpatterns = [
    path('v3',  ProductGenericsView.as_view()),
]

