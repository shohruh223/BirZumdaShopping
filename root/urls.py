from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from app.views.auth_forgot import ForgotPasswordView, ResetPasswordView
from app.views.others import IndexView, MahsulotlarView, MahsulotlarDetailView
from app.views.auth import RegisterView, UserLoginView, UserLogoutView, VerifyEmailView
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
    path('verify/', VerifyEmailView.as_view(), name='verify-email'),

    # forgot password
    path('forgot-password/', ForgotPasswordView.as_view(), name='forgot-password'),
    path('reset-password/', ResetPasswordView.as_view(), name='reset-password'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
