from django.conf.urls.static import static
from django.urls import path
from alotechh import settings
from . import views


urlpatterns = [
    path('', views.home_view, name='home'),
    path('search-listing', views.search_view, name='search-listing'),
    ]



