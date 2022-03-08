from django.urls import path
from . import views

app_name = "about"

urlpatterns = [
    path('', views.about_index_view),
    path('contact/', views.about_contact_view)
]
