from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework import routers
from ida_dialog.views import IdaDialogViewSet
from ida_start.views import IdaStartView

router = routers.DefaultRouter()
router.register(r'dados', IdaDialogViewSet)
router.register(r'start', IdaStartView)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
