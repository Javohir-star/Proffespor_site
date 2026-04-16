from django.urls import path
from apps.users.view import home

from apps.users.views.user import (
    UserCreateAPIView,
    UserListAPIView,
    UserRetrieveAPIView,
    UserUpdateAPIView,
    UserDestroyAPIView,
)

urlpatterns = [
    path("",home,name="home"),
    path("users/", UserListAPIView.as_view(), name="user-list"),
    path(
        "users/<int:pk>/",
        UserRetrieveAPIView.as_view(),
        name="user-detail",
    ),
    path("users/create/", UserCreateAPIView.as_view(), name="user-create"),
    path("users/update/<int:pk>/", UserUpdateAPIView.as_view(), name="user-update"),
    path("users/delete/<int:pk>/", UserDestroyAPIView.as_view(), name="user-delete"),
]