from django.urls import path
from misha1 import views
urlpatterns = [
    path('',views.homepage),
    path('about/',views.about,name='Rasul'),
    path('contacts/',views.contacts,name='Misha')

]