from django.urls import path,reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView

from users.views import UsercreateView





app_name = 'users'
urlpatterns = [
    path('login/', LoginView.as_view( next_page = reverse_lazy('core:home'), redirect_authenticated_user=True), name = 'user-login'),
    path('logout/', LogoutView.as_view(next_page = reverse_lazy('users:user-login')), name = 'user-logout'),
    path('register/', UsercreateView.as_view(), name = 'user-register'),
]