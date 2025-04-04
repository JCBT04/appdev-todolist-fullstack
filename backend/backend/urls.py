from django.urls import path
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('todo.urls')),
    path('', RedirectView.as_view(url='/api/', permanent=False)),  # Redirect root to /api/
]
