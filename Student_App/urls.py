from django.contrib import admin
from django.urls import path
# from .views import StudentsView
from .views import StudentView

urlpatterns = [
    path('studentapi/', StudentView.as_view()),
    path('studentapi/<int:pk>', StudentView.as_view())
]
