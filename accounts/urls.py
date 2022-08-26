from django.urls import path
from accounts.views import *
app_name = 'signup'
urlpatterns = [
     path('signup',signup_view, name='signup'),
]
