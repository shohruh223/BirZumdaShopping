from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from app.utils import generate_code, send_register_email

User = get_user_model()


class ForgotPasswordView(TemplateView):
    template_name = 'forgot-password.html'

    def post(self, request, *args, **kwargs):
        email = request.POST.get('email')

        user = User.objects.filter(email=email).first()
        if not user:
            return render(request, self.template_name,
                          {'error': 'Bunday foydalanuvchi topilmadi'})

        code = generate_code()
        request.session['reset_code'] = code
        request.session['reset_user_id'] = user.id
        send_register_email(user.email, code)
        return redirect('reset-password')


class ResetPasswordView(TemplateView):
    template_name = 'reset-password.html'

    def post(self, request, *args, **kwargs):
        code = request.POST.get('code')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if code != str(request.session.get('reset_code')):
            return render(request, self.template_name, {'error': 'Kod noto‘g‘ri'})

        if password != confirm_password:
            return render(request, self.template_name, {'error': 'Parollar bir xil emas'})

        user = User.objects.filter(id=request.session.get('reset_user_id')).first()
        if not user:
            return redirect('forgot-password')

        user.set_password(password)
        user.save()

        request.session.pop('reset_code', None)
        request.session.pop('reset_user_id', None)

        return redirect('login')