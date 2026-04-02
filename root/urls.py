from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from app.views import IndexView, MahsulotlarView, MahsulotlarDetailView
from root import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('mahsulotlar/', MahsulotlarView.as_view(), name='mahsulotlar'),
    path('mahsulotlar-detail/<int:pk>/', MahsulotlarDetailView.as_view(), name='mahsulotlar-detail'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
