from django.contrib import admin
from django.urls import path
from .views import Home, About, Upload, login_user, logout_user, signup_user, show_product
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('', Home , name ="home"),
    path('about', About , name ="about"),
    path('upload', Upload, name= "upload"),
    path('login', login_user, name='login'),
    path('signup', signup_user, name='signup'),
    path('logout', logout_user, name='logout'),
    path('product/<int:id>', show_product, name='product'),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)