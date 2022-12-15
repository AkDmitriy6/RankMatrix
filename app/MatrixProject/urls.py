from django.conf.urls.static import static
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from MatrixProject import settings

urlpatterns = [
    #path("admin/", admin.site.urls),
    path('', include('rankapp.urls')),
    path('api/', include('api.urls')),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path(
        'docs/',
        SpectacularSwaggerView.as_view(
            url_name="schema",
        ),
        name="swagger-ui",
    )
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

