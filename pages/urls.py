from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    path('about/', views.AboutPageView.as_view(), name='about'),
    path('contact-us/', views.ContactUsPageView.as_view(), name='contact'),
    path('faq/', views.FaqPageView.as_view(), name='faq'),
    path('privacy/', views.PrivacyPageView.as_view(), name='privacy'),
    path('our-services/', views.OurServicesPageView.as_view(), name='our_services'),
]
