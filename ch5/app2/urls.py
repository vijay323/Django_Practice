from django.urls import path
from app2 import views as ap2
urlpatterns = [
    path('php/',ap2.learn_php,name='LearnPHP')
]
