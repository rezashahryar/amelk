from django.views import generic

# Create your views here.


class AboutPageView(generic.TemplateView):
    template_name = 'pages/about.html'


class ContactUsPageView(generic.TemplateView):
    template_name = 'pages/contact_us.html'


class FaqPageView(generic.TemplateView):
    template_name = 'pages/faq.html'


class PrivacyPageView(generic.TemplateView):
    template_name = 'pages/privacy.html'
