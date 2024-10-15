from django.urls import path
from .views import register
from .views import login_view
from .views import home
from .views import logout
from .views import landing



urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('home/', home, name='home'),
    path('logout/', logout, name='logout'),
    path('', landing, name='landing'),
   
]
