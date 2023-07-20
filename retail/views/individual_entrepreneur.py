from rest_framework import permissions
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView

from retail.models import IndividualEntrepreneur
from retail.serializers import IndividualEntrepreneurSerializer, IndividualEntrepreneurWithContactsSerializer


class IndividualEntrepreneurCreateView(CreateAPIView):
    serializer_class = IndividualEntrepreneurSerializer
    permission_classes = [permissions.IsAuthenticated]


class IndividualEntrepreneurListView(ListAPIView):
    serializer_class = IndividualEntrepreneurWithContactsSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = IndividualEntrepreneur.objects.all()
        country = self.request.query_params.get('country')
        if country is not None:
            queryset = queryset.filter(contacts__country=country.upper())
        return queryset


class IndividualEntrepreneurDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = IndividualEntrepreneurSerializer
    permission_classes = [permissions.IsAuthenticated]


