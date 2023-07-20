
from django.urls import path, include
from rest_framework.routers import SimpleRouter

from retail.views.views import ContactsView, ProductsView, RegistrationView, ProfileView

from retail.views.factory import FactoryCreateView, FactoryListView, FactoryDetailView
from retail.views.individual_entrepreneur import IndividualEntrepreneurCreateView, IndividualEntrepreneurListView, \
    IndividualEntrepreneurDetailView
from retail.views.retail_network import RetailNetworkDetailView, RetailNetworkListView, RetailNetworkCreateView


router = SimpleRouter()
router.register("contact", ContactsView)
router.register("product", ProductsView)

urlpatterns = [
    path("", include(router.urls)),

    path("factory/create", FactoryCreateView.as_view()),
    path("factory/list", FactoryListView.as_view()),
    path("factory/<int:pk>", FactoryDetailView.as_view()),

    path("retail_network/create", RetailNetworkCreateView.as_view()),
    path("retail_network/list", RetailNetworkListView.as_view()),
    path("retail_network/<int:pk>", RetailNetworkDetailView.as_view()),

    path("ei/create", IndividualEntrepreneurCreateView.as_view()),
    path("ei/list", IndividualEntrepreneurListView.as_view()),
    path("ei/<int:pk>", IndividualEntrepreneurDetailView.as_view()),

    path("signup", RegistrationView.as_view()),
    path("profile", ProfileView.as_view())
]
