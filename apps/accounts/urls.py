from django.urls import path
from apps.accounts.views import SignUpView, login_view

app_name = 'accounts'

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', login_view, name='login')
]