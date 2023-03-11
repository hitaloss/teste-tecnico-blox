from django.urls import path
from . import views


urlpatterns = [
    path("account/", views.AccountView.as_view()),
    path("account/<int:pk>/balance/", views.AccountBalanceDetailView.as_view()),
    path("account/<int:pk>/flag/", views.AccountActiveDetailView.as_view()),
]
