from django.urls import path
from . import views


urlpatterns = [
    path("account/<int:pk>/deposit/", views.DepositView.as_view()),
    path("account/<int:pk>/withdraw/", views.WithdrawView.as_view()),
]
