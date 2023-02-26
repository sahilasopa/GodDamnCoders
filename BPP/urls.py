from django.urls import path

from BPP import views as bpp
from JobsPortal import views as jobs

urlpatterns = [
    path('', bpp.home),
    path('search', bpp.search),
]
