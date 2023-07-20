from typing import Any

from django.contrib.auth import get_user_model, logout
from django.contrib.auth.models import User
from rest_framework import viewsets, generics, permissions, status
from rest_framework.response import Response

from retail.models import Contacts, Products
from retail.serializers import ContactsSerializer, ProductsSerializer, RegistrationSerializer, UserSerializer


class ProductsView(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer


class ContactsView(viewsets.ModelViewSet):
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer


class RegistrationView(generics.CreateAPIView):
    queryset = User
    permission_classes = [permissions.AllowAny]
    serializer_class = RegistrationSerializer


class ProfileView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self) -> Any:
        return self.request.user

    def delete(self, request: Any, *args: Any, **kwargs: Any) -> Any:
        logout(request)
        return Response(status=status.HTTP_204_NO_CONTENT)
