from django.urls import path
from course import views as c1
urlpatterns = [
    path('home/',c1.home,name='home'),
    path('dj/',c1.django,name='dj'),
    path('py/',c1.python,name='py')
]
