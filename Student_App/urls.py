from django.contrib import admin
from django.urls import path
# from .views import StudentsView
from .views import AllStudentView, SingleStudentView

urlpatterns = [
    path('studentapi/', AllStudentView.as_view()),
    path('studentapi/<int:pk>/', SingleStudentView.as_view())
]
