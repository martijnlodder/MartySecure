from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.deprecation import MiddlewareMixin


class MFAMiddleware(MiddlewareMixin):
    def process_view(self, request, view_func, view_args, view_kwargs):
        if request.user.is_authenticated and not request.user.is_verified():
            if 'otp_device_id' in request.session:
                return None
            return redirect(reverse_lazy('mfa_authenticate'))
        return None
