from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from app.serializers import (
    InvoiceSerializers, ItemSerializers, RequirementSerializers
)

from app.models import Invoice, Item, Requirements


class InvoiceViewSet(ModelViewSet):
    """ Invoice model Viewset """
    serializer_class = InvoiceSerializers
    authentication_classes = [TokenAuthentication,]
    permission_classes = [IsAuthenticated,]

    def get_queryset(self):
        queryset = Invoice.objects.filter(user_create=self.request.user)
        return queryset

    def perform_create(self, serializer):
        """ Create a new invoice """
        serializer.save(user_create=self.request.user)


class ItemViewSet(ModelViewSet):
    """ Item model Viewset """
    serializer_class = ItemSerializers
    authentication_classes = [TokenAuthentication,]
    permission_classes = [IsAuthenticated,]

    def get_queryset(self):
        queryset = Item.objects.filter(user_create=self.request.user)
        return queryset

    def perform_create(self, serializer):
        """ Create a new item """
        serializer.save(user_create=self.request.user)


class RequirementViewset(ModelViewSet):
    """ Requirements model Viewset """
    serializer_class = RequirementSerializers
    authentication_classes = [TokenAuthentication,]
    permission_classes = [IsAuthenticated,]

    def get_queryset(self):
        queryset = Requirements.objects.filter(user_create=self.request.user)
        return queryset

    def perform_create(self, serializer):
        serializer.save(user_create=self.request.user)