from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.user_login), # localhost:8000/account/login 경로, 경로를 호출하면 실행할 함수의
]