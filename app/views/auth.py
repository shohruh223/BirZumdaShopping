from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, TemplateView
from app.form import RegisterForm, EmailLoginForm
from app.utils import generate_code, send_register_email
from django.contrib.auth import get_user_model


User = get_user_model()


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = "register.html"
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        super().form_valid(form)

        user = self.object
        code = generate_code()
        # Kodni va Userni sessionda saqlaymiz
        self.request.session["verify_user_id"] = user.id
        self.request.session["verify_code"] = str(code)
        send_register_email(to_email=user.email, code=code)

        return redirect("verify-email")


class UserLoginView(LoginView):
    authentication_form = EmailLoginForm
    template_name = "login.html"
    redirect_authenticated_user = True


class UserLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("login")

    def post(self, request):
        logout(request)
        return redirect("login")


class VerifyEmailView(TemplateView):
    template_name = "confirm-password.html"

    def post(self, request, *args, **kwargs):
        if request.POST.get("code") != request.session.get("verify_code"):
            return redirect("verify-email")

        user = User.objects.get(id=request.session["verify_user_id"])
        user.is_active = True
        user.save()

        request.session.pop("verify_code", None)
        request.session.pop("verify_user_id", None)
        return redirect("login")

