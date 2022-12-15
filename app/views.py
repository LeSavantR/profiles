import io

from django.core.exceptions import ObjectDoesNotExist
from django.http import FileResponse, HttpRequest

from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from app.models import Invoice, Item
from app.serializers import (
    InvoiceSerializers, ItemSerializers
)


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


def fac_pdf(request: HttpRequest, pk: str):
    if pk is None:
        return
    
    try:
        fac = Invoice.objects.get(id=pk)
        bytes = io.BytesIO()
        pdf = canvas.Canvas(bytes, pagesize=landscape(letter))
        
        pdf.showPage()
        pdf.save()
        bytes.seek(0)

        return FileResponse(
            pdf, as_attachment=True,
            filename=f'{fac.date.strftime("%d%m%Y")}.pdf'
        )

    except ObjectDoesNotExist:
        return


def cot_pdf(request: HttpRequest, pk: str):
    if pk is None:
        return

    try:
        pass
    except:
        pass


def req_pdf(request: HttpRequest, pk: str):
    if pk is None:
        return

    try:
        pass
    except:
        pass
