from rest_framework.serializers import (
    ListSerializer, ModelSerializer, StringRelatedField
)

from app.models import Invoice, Item
from profiles.serializers import UserProfileSerializer


class InvoiceSerializers(ModelSerializer):
    """ Invoice Serializer """
    user_create = StringRelatedField(read_only=True)

    class Meta:
        model = Invoice
        fields = '__all__'


class ItemList(ListSerializer):
    """ Item List Serializer """
    invoice = StringRelatedField(many=False, read_only=True)
    user_create = StringRelatedField(read_only=True)

    class Meta:
        model = Item
        fields = [
            'invoice', 'title', 'context',
            'materials', 'method', 'value',
            'user_create', 'date_created',
        ]
        extra_kwargs = {
            'user_create' : {'read_only': True},
            'date_created' : {'read_only': True},
        }


class ItemSerializers(ModelSerializer):
    """ Items Serializers """
    user_create = StringRelatedField(read_only=True)
    invoice = StringRelatedField(many=False, read_only=True)

    class Meta:
        model = Item
        list_serializer_class = ItemList
        fields = [
            'invoice', 'title', 'context',
            'materials', 'method', 'value',
            'user_create', 'date_created',
        ]
        extra_kwargs = {
            'user_create' : {'read_only': True},
            'date_created' : {'read_only': True},
        }
