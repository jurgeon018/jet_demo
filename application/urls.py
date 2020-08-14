from django.urls import include, path
from django.contrib import admin
from jet.dashboard.dashboard_modules import google_analytics_views


urlpatterns = [
    path('jet/', include('jet.urls', 'jet')),
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
]
