from django.urls import path
from . import views

urlpatterns = [
    path('',views.disp,name="disp"),
    path('add/',views.add,name="add"),
    path('Edit/',views.Edit,name="Edit"),
    path('delete/',views.delete,name="delete"),
]
