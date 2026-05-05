from django.urls import path
from course import views
urlpatterns = [
    path('vijay/',views.vijay,name='vijay'),
    path('dj/',views.dj,name='django'),
    path('fast/',views.fast,name='api')
]
