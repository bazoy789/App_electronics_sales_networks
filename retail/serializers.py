from typing import Optional, Any

from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers

from retail.models import Factory, Contacts, Products, RetailNetwork, IndividualEntrepreneur

USER_MODEL = get_user_model()


class ContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = "__all__"


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = "__all__"


class FactorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Factory
        fields = "__all__"
        read_only_fields = ["arrears"]


class FactoryWithContactsSerializer(serializers.ModelSerializer):
    contacts = ContactsSerializer()
    class Meta:
        model = Factory
        fields = "__all__"
        read_only_fields = ["arrears"]


class RetailNetworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = RetailNetwork
        fields = "__all__"
        read_only_fields = ["arrears"]


class RetailNetworkWithContactsSerializer(serializers.ModelSerializer):
    contacts = ContactsSerializer()

    class Meta:
        model = RetailNetwork
        fields = "__all__"
        read_only_fields = ["arrears"]


class IndividualEntrepreneurSerializer(serializers.ModelSerializer):

    class Meta:
        model = IndividualEntrepreneur
        fields = "__all__"
        read_only_fields = ["arrears"]


class IndividualEntrepreneurWithContactsSerializer(serializers.ModelSerializer):
    contacts = ContactsSerializer()

    class Meta:
        model = IndividualEntrepreneur
        fields = "__all__"
        read_only_fields = ["arrears"]


class PasswordField(serializers.CharField):

    def __init__(self, **kwargs: Optional[Any]) -> None:
        kwargs["style"] = {"input_type": "password"}
        kwargs.setdefault("write_only", True)
        super().__init__(**kwargs)
        self.validators.append(validate_password)


class RegistrationSerializer(serializers.ModelSerializer):
    password = PasswordField(required=True)

    class Meta:
        model = USER_MODEL
        read_only_fields = ("id",)
        fields = ("id", "username", "password")

    def create(self, validated_data: dict) -> dict:
        validated_data["password"] = make_password(validated_data["password"])
        return super().create(validated_data)


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = USER_MODEL
        fields = ("id", "username", "first_name", "last_name", "email")