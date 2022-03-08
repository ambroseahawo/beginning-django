from django.urls import path
from . import views


app_name = "stores"

urlpatterns = [
    path('<int:store_id>/', views.stores_detail_view,name="detail"),
    path('', views.stores_list_view,name="index"),
]
