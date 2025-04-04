from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView  # For static views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('todo.urls')),  # Keep this for the /api/
    path('', TemplateView.as_view(template_name='index.html')),  # Serve a static page at the root
]
