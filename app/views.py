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
    queryset = Invoice.objects.all()
    authentication_classes = [TokenAuthentication,]
    permission_classes = [IsAuthenticated,]

    def perform_create(self, serializer):
        """ Create a new invoice """
        serializer.save(user_create=self.request.user)


class ItemViewSet(ModelViewSet):
    """ Item model Viewset """
    serializer_class = ItemSerializers
    queryset = Item.objects.all()
    authentication_classes = [TokenAuthentication,]
    permission_classes = [IsAuthenticated,]

    def perform_create(self, serializer):
        """ Create a new item """
        serializer.save(user_create=self.request.user)


class RequirementViewset(ModelViewSet):
    """ Requirements model Viewset """
    serializer_class = RequirementSerializers
    queryset = Requirements.objects.all()
    authentication_classes = [TokenAuthentication,]
    permission_classes = [IsAuthenticated,]

    def perform_create(self, serializer):
        serializer.save(user_create=self.request.user)