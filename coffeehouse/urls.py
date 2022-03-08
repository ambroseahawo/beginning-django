from django.contrib import admin
from django.urls import path, include

from django.views.generic import TemplateView

# granular urls first, broad urls last
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='homepage.html'),name="homepage"),
    path('about/', include("about.urls", namespace="about")),
    path('stores/', include("stores.urls", namespace="stores"), { "location": "headquarters" }),
]