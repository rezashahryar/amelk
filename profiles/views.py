from django.shortcuts import render

# Create your views here.


def profile_index_page_view(request):
    return render(request, 'profiles/index.html')


def profile_favorite_view(request):
    return render(request, 'profiles/profile_favorites.html')


def add_house_case_view(request):
    return render(request, 'profiles/add_house_case.html')

def house_list_view(request):
    return render(request, 'profiles/house_list.html')
