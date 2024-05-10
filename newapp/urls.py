from django.urls import path
from . import views


urlpatterns = [
    path('',views.sample,name="sample"),
    path('add/',views.add,name="add"),
    path('addrec/',views.addrec,name="addrec"),
    path('delete/<id>/',views.delete,name="delete"), 
    path('update/<id>/',views.update,name="update"),            
]