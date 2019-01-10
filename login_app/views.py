from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.shortcuts import render


# Create your views here.
class IndexView(View):
    def get(self, request, *args, **kwargs):
        context = {'parm1': 'hello', 'parm2': 'django', 'auth': request.user.is_authenticated}
        print(request.user)
        return render(request, 'index.html', context=context)

@login_required
def profile(request):
    data = {'last_login': request.user.last_login, 'username': request.user.username,
            'password': request.user.password, 'is_authenticated': request.user.is_authenticated}
    return render(request, 'login_app/profile.html', context={'data': data})

