from django.contrib import admin
from django.urls import path
from .views import (HaluView, HaluCreateView, Detail, HaluUpdateView, HaluDeleteView, Detail_ten,
 Grade_ten_create_view, Grade_ten_list_view, TenUpdateView, TenDeleteView)

urlpatterns=[
    path("create/", HaluCreateView.as_view(), name="create"),
    path("", HaluView.as_view(), name="points"),
    path("points/<int:pk>/", Detail.as_view(), name="detail_school"),
    path("points/<int:pk>/edit", HaluUpdateView.as_view(), name="update"),
    path("points/<int:pk>/delete", HaluDeleteView.as_view(), name="delete"),
    path("ten/<int:pk>/", Detail_ten.as_view(), name="detail_ten"),
    path("ten/create", Grade_ten_create_view.as_view(), name="create_ten"),
    path("ten/list", Grade_ten_list_view.as_view(), name="list_ten"),
    path("ten/<int:pk>/edit", TenUpdateView.as_view(), name="update_ten"),
    path("ten/<int:pk>/delete", TenDeleteView.as_view(), name="delete_ten"),
]