from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import StudentModel
from .serializers import StudentSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, \
    RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser, \
    IsAuthenticatedOrReadOnly, DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from .CustomAuth import CustomAuth


# Create your views here.

class StudentViewSet(viewsets.ModelViewSet):
    queryset = StudentModel.objects.all()
    serializer_class = StudentSerializer
    # =======Authentications=====
    # authentication_classes = [BasicAuthentication] # Never use in deployment.
    # authentication_classes = [SessionAuthentication]
    authentication_classes = [CustomAuth]
    # by admin panel token generate.
    # by cmd ---python manage.py drf_create_token user_1
    # by exposing an api endpoint By user.

    # ====== Permissions=========
    permission_classes = [IsAuthenticated]
    # permission_classes = [AllowAny]
    # when is staff is true.
    # permission_classes = [IsAdminUser]
    # permission_classes = [IsAuthenticatedOrReadOnly]
    # for custom permissions from Admin site.
    # permission_classes = [DjangoModelPermissions]
    # same as django model permissions but unauthenticated user have view only.
    # permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

# Custom Token creator /gettoken is called by user
# class CustomAuthToken(ObtainAuthToken):
#
#     def post(self, request, *args, **kwargs):
#         serializer = self.serializer_class(data=request.data,
#                                            context={'request': request})
#         serializer.is_valid(raise_exception=True)
#         user = serializer.validated_data['user']
#         token, created = Token.objects.get_or_create(user=user)
#         return Response({
#             'token': token.key,
#             'user_id': user.pk,
#             'email': user.email
#         })
