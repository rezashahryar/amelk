from django.urls import path
from . import views


app_name = 'profiles'

urlpatterns = [
    path('', views.profile_index_page_view, name='index'),
    path('favorites/', views.profile_favorite_view, name='favorites'),
    path('add/house/', views.add_house_case_view, name='add_house'),
    path('list/house/', views.house_list_view, name='list_house'),
]
