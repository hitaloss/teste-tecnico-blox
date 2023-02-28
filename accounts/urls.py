from django.urls import path
from drf_spectacular.views import SpectacularSwaggerView
from . import views


urlpatterns = [
    path("account/", views.AccountCreateView.as_view()),
    path("account/<int:pk>/balance/", views.AccountBalanceDetailView.as_view()),
    path("account/schema/swagger-ui/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
]
