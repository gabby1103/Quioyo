from django.urls import path
from .views import HomePageView, AboutPageView, FavPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about', AboutPageView.as_view(), name='about'),
    path('fav', FavPageView.as_view(), name='fav'),
]