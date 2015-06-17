from django.conf.urls import include, url
from django.views.generic.base import RedirectView, TemplateView

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='home'),
    url(r'^f/(?P<path>.*)', RedirectView.as_view(url='http://files.consumerfinance.gov/f/%(path)s')),


    url(r'^blog/$', TemplateView.as_view(template_name='blog/index.html'), name='blog_index'),
    url(r'^blog/(?P<slug>[\w-]+)/$', 'flapjack.views.blog_detail', name='blog_detail'),
]
