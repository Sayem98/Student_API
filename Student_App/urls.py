from django.contrib import admin
from django.urls import path, include
# from .views import StudentsView
from .views import StudentViewSet # CustomAuthToken
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

# creating router object.
router = DefaultRouter()

# Registering StudentViewSet with router.

router.register('studentapi', StudentViewSet, basename='student')


urlpatterns = [
    path('', include(router.urls)),
    # adds login and logout system in our api.
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    # path('gettoken/', CustomAuthToken.as_view()),
    path('gettoken/', TokenObtainPairView.as_view(), name='token-obtain-pair'),
    path('refreshtoken/', TokenRefreshView.as_view(), name='token-refresh'),
    path('verifytoken/', TokenVerifyView.as_view(), name='verify-token')
]
