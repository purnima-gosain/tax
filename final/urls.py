from django.urls import path

from . import views

urlpatterns = [
    path('',views.home, name='index.html'),
    path('post',views.post , name="tax.html")  
]
