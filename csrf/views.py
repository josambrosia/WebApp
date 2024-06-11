from django.contrib.auth.views import LogoutView, LoginView
from django.contrib import messages
from django.shortcuts import redirect
from django.utils.decorators import method_decorator

class UserLoginView(LoginView):
    template_name = 'users/login.html'
    redirect_authenticated_user = True


class UserLogoutView(LogoutView):
    # template_name = 'users/logout.html'

    # print('iam here')
    # def get(self, request, *args, **kwargs):
    #     print(self.request)
    #     print('oioi')

    def get_next_page(self):
        # print(self.request.session.values())
        # if self.request.user.is_authenticated:
        next_page = super(UserLogoutView, self).get_next_page()
        # messages.success(self.request, f'Kamu telah berhasil logout !')
        return next_page #ini mengeksekusi variable `next_page` di parent class yg mana mengarah ke setting.LOGOUT_REDIRECT_URL
        # else:
        #     next_page = super(UserLogoutView, self).get_next_page()
        #     messages.warning(self.request, 'Hah ???')
        #     return next_page