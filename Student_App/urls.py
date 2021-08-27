from django.contrib import admin
from django.urls import path
# from .views import StudentsView
from .views import StudentListView, StudentCreateView,\
    StudentRetrieveView, StudentUpdateView, StudentDestroyView, StudentLCView, StudentRUDView

urlpatterns = [
    # path('studentapi/', StudentListView.as_view()),
    # path('studentapi/', StudentCreateView.as_view()),
    path('studentapi/', StudentLCView.as_view()),
    # path('studentapi/<int:pk>/', StudentRetrieveView.as_view()),
    # path('studentapi/<int:pk>/', StudentUpdateView.as_view()),
    # path('studentapi/<int:pk>/', StudentDestroyView.as_view()),
    path('studentapi/<int:pk>/', StudentRUDView.as_view()),

]
