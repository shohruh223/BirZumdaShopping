from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from app.views import IndexView, MahsulotlarView, MahsulotlarDetailView, RegisterView, UserLoginView, UserLogoutView
from root import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('mahsulotlar/', MahsulotlarView.as_view(), name='mahsulotlar'),
    path('mahsulotlar-detail/<int:pk>/', MahsulotlarDetailView.as_view(), name='mahsulotlar-detail'),


    # register
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
