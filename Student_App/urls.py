from django.contrib import admin
from django.urls import path, include
# from .views import StudentsView
from .views import StudentViewSet
from rest_framework.routers import DefaultRouter

# creating router object.
router = DefaultRouter()

# Registering StudentViewSet with router.

router.register('studentapi', StudentViewSet, basename='student')


urlpatterns = [
    path('', include(router.urls))
]
