
import django_filters
from rest_framework import permissions
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView

from retail.models import Factory
from retail.serializers import FactorySerializer, FactoryWithContactsSerializer


class FactoryCreateView(CreateAPIView):
    serializer_class = FactorySerializer
    permission_classes = [permissions.IsAuthenticated]


class FactoryListView(ListAPIView):
    serializer_class = FactoryWithContactsSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = Factory.objects.all()
        country = self.request.query_params.get('country')
        if country is not None:
            queryset = queryset.filter(contacts__country=country.upper())
        return queryset


class FactoryDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = FactorySerializer
    permission_classes = [permissions.IsAuthenticated]

