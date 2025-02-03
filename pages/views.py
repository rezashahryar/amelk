from django.views import generic

# Create your views here.


class HomePageView(generic.TemplateView):
    template_name = 'pages/home.html'


class AboutPageView(generic.TemplateView):
    template_name = 'pages/about.html'


class ContactUsPageView(generic.TemplateView):
    template_name = 'pages/contact_us.html'


class FaqPageView(generic.TemplateView):
    template_name = 'pages/faq.html'


class PrivacyPageView(generic.TemplateView):
    template_name = 'pages/privacy.html'


class OurServicesPageView(generic.TemplateView):
    template_name = 'pages/our_services.html'
