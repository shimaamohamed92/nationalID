from django.urls import path, include
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from nationalid.users.views import (
    user_detail_view,
    user_redirect_view,
    user_update_view,
    NationalCreateAPI,
)

app_name = "users"


urlpatterns = [
    path("~redirect/", view=user_redirect_view, name="redirect"),
    path("~update/", view=user_update_view, name="update"),
    path("<str:username>/", view=user_detail_view, name="detail"),
    path('nationalids/<int:pk>/', NationalCreateAPI.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)