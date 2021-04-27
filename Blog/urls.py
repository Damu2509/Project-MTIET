from django.urls import path
from .views import home

urlpatterns = [
    path('blog/', home, name = 'home')
]