from typing import Any

from django.contrib.auth import get_user_model, logout
from rest_framework import viewsets, generics, permissions, status
from rest_framework.response import Response

from retail.models import Contacts, Products
from retail.serializers import ContactsSerializer, ProductsSerializer, RegistrationSerializer, UserSerializer

USER_MODEL = get_user_model()


class ProductsView(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer


class ContactsView(viewsets.ModelViewSet):
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer


class RegistrationView(generics.CreateAPIView):
    queryset = USER_MODEL
    permission_classes = [permissions.AllowAny]
    serializer_class = RegistrationSerializer


class ProfileView(generics.RetrieveUpdateDestroyAPIView):
    queryset = USER_MODEL.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self) -> Any:
        return self.request.user

    def delete(self, request: Any, *args: Any, **kwargs: Any) -> Any:
        logout(request)
        return Response(status=status.HTTP_204_NO_CONTENT)
