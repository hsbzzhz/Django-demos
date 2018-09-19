from django.urls import include,path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'HireTest'
urlpatterns = [

    path('', views.index, name ='main-index'),
    path('search/', views.search,name = 'search'),
    path('profile/', views.profile, name = 'profile'),


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
