from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # Authentication URLs for Password Reset
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('store.urls')),
    path('analytics/', include('analytics.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
