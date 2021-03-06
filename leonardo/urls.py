from django.urls import path

from . import views
from django.views.generic import TemplateView


urlpatterns = [
    path('leonardo/komiteer/', views.komiteer, name='komiteer'),
    path('leonardo/komiteer/<slug:komite_slug>',
         views.komite_detail, name='komite_detail'),
    path('leonardo/om-leonardo/', views.about, name='about'),
    path('leonardo/vedtekter/', views.vedtekter, name='vedtekter'),
    path('leonardo/thesign/', views.thesign, name='thesign'),
    path('folketinget', TemplateView.as_view(template_name="leonardo/folketinget.html"), name="folketinget")
]
