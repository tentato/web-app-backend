from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.main, name='main'),
    path('tabs/', views.tabs, name='tabs'),
    path('tabs/details/<int:id>', views.details, name='details'),
    

    path('testing/', views.testing, name='testing'), 
     
]

urlpatterns += staticfiles_urlpatterns()