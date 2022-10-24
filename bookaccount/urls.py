from django.urls import path
from .views import Signupwive

urlpatterns = [
    path('signup/', Signupwive.as_view(), name='signup'),
]

