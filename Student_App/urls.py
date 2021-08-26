from django.contrib import admin
from django.urls import path
from .views import StudentsView

urlpatterns = [
    path('studentapi/', StudentsView),
    path('studentapi/<int:pk>', StudentsView)
]
