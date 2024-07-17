from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('register', views.register_view, name='register'),
    path('update_user_location', views.update_user_location, name='update_user_location'),
    path('map', views.map_view, name='map'),  # Ensure this line is added
]
