from django.urls import path
from . import views


app_name = 'profiles'

urlpatterns = [
    path('', views.profile_index_page_view, name='index'),
    path('favorites/', views.profile_favorite_view, name='favorites'),
]
