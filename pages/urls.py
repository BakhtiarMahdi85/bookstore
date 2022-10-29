from django.urls import path
from .views import HomepageViews


urlpatterns = [
    path('', HomepageViews.as_view(), name='home')
]