from django.urls import path
from .views import HomepageViews


urlpatterns = [
    path('home/', HomepageViews.as_view(), name='home')
]