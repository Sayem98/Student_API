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
    path('', include(router.urls)),
    # adds login and logout system in our api.
    path('auth/', include('rest_framework.urls', namespace='rest_framework'))
]
