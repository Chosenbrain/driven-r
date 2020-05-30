

from django.contrib import admin
from django.urls import path
from website.views import index,portfolio,services,contact,about

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('portfolio/', portfolio, name='portfolio'),
    path('services/', services, name='services'),
    path('contact/', contact, name='contact'),
    path('about/', about, name='about')
]

