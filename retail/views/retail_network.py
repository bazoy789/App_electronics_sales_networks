from rest_framework import permissions
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView

from retail.models import RetailNetwork
from retail.serializers import RetailNetworkSerializer, RetailNetworkWithContactsSerializer


class RetailNetworkCreateView(CreateAPIView):
    serializer_class = RetailNetworkSerializer
    permission_classes = [permissions.IsAuthenticated]


class RetailNetworkListView(ListAPIView):
    serializer_class = RetailNetworkWithContactsSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = RetailNetwork.objects.all()
        country = self.request.query_params.get('country')
        if country is not None:
            queryset = queryset.filter(contacts__country=country.upper())
        return queryset


class RetailNetworkDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = RetailNetworkSerializer
    permission_classes = [permissions.IsAuthenticated]
