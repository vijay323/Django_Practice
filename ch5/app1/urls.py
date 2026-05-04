from django.urls import path
from app1 import views as ap1

urlpatterns = [
    path('dj/',ap1.learn_django)
]
