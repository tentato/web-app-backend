from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.main, name='main'),
    path('tabs/', views.tabs, name='tabs'),
    path('tabs/tab_details/<int:id>', views.tab_details, name='tab_details'),
    path('posts/', views.posts, name='posts'),
    path('posts/post_details/<int:id>', views.post_details, name='post_details'),

    path("contact/", views.contact_view, name="contact"),
    

    path('testing/', views.testing, name='testing'), 
     
]

urlpatterns += staticfiles_urlpatterns()