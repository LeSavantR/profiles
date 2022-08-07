from django.db import models
from django.conf import settings
from django.db.models import Q


class Modelo(models.Model):
    """
        Base Model:
        - Enabled.
        - User Created.
        - Created Date.
        - Modified Date.
    """
    enabled = models.BooleanField(
        verbose_name='Habilitado?',
        default=True,
    )
    user_create = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        help_text='Usuario que creo el registro.',
    )
    date_created = models.DateTimeField(
        verbose_name='Fecha de creación',
        auto_now_add=True,
        help_text='Fecha de creación del registro.',
    )
    date_modify = models.DateTimeField(
        verbose_name='Fecha de modificación',
        auto_now=True,
        help_text='Fecha de modificación del registro.',
    )

    class Meta:
        abstract = True


class Invoice(Modelo):
    """
        Invoice Model:
        - Invoice Number.
        - Invoice Date.
        - Invoice Value Verbose.
        - Invoice Sub-Value.
        - Invoice Value Discount.
        - Invoice Total Value.
        - @P Items.
    """
    invoice_num = models.IntegerField(
        verbose_name='Consecutivo', blank=True,
        help_text='Consecutivo de factura.',
    )
    date = models.DateField(
        verbose_name='Fecha',
        help_text='Fecha de cobro de factura.',
    )
    value_verbose = models.CharField(
        verbose_name='Valor',
        max_length=100, blank=True, null=True,
        help_text='Valor en texto de la factura.',
    )
    sub_value = models.IntegerField(
        verbose_name='Subtotal',
        blank=True, null=True,
        help_text='Valor Subtotal.',
    )
    discount = models.IntegerField(
        verbose_name='Descuento en %',
        blank=True, null=True,
        help_text='Valor descuento en pesos.',
    )
    total_value = models.IntegerField(
        verbose_name='Valor Total',
        blank=True, null=True,
        help_text='Valor total a cobrar.',
    )

    @property
    def items(self):
        return self.item_set.all()

    def __str__(self):
        return f'{self.invoice_num} - {self.date}'

    class Meta:
        verbose_name = 'Factura'
        verbose_name_plural = 'Facturas'


class Item(Modelo):
    """
        Item Model:
        - Item Invoice.
        - Item Title.
        - Item Description.
        - Item Materials.
        - Item Methods.
        - Item Value.
    """
    invoice = models.ForeignKey(
        Invoice, on_delete=models.SET_NULL,
        verbose_name='Factura', null=True, blank=True,
        help_text='Factura a la que pertenece la Cotizacion.',
    )
    title = models.CharField(
        verbose_name='Titulo',
        max_length=100, blank=False,
        help_text='Titulo de la cotizacion.',
    )
    context = models.TextField(
        verbose_name='Descripción',
        max_length=500, blank=False,
        help_text='Descripción de la cotizacion.',
    )
    materials = models.CharField(
        verbose_name='Materiales',
        max_length=200, blank=True,
        help_text='Materiales de la cotizacion.',
        default='Los Necesarios'
    )
    method = models.CharField(
        verbose_name='Cobro',
        max_length=100, blank=False,
        help_text='Cobro de la cotizacion.',
    )
    value = models.IntegerField(
        verbose_name='Valor', blank=False,
        help_text='Valor de la cotizacion.',
    )

    def __str__(self):
        return f'{self.title} - {self.date_created.strftime("%d/%m/%Y")}'

    class Meta:
        verbose_name = 'Cotizacion'
        verbose_name_plural = 'Cotizaciones'


class Requirements(Modelo):
    """
        Required Model:
        - Item Model.
    """
    item = models.OneToOneField(
        Item, on_delete=models.CASCADE,
        verbose_name='Cotizacion',
        help_text='Cotizacion a la que pertenece el Requerimiento.',
    )

    def __str__(self) -> str:
        return f'{self.item.__str__} - Requerimiento'

    class Meta:
        verbose_name = 'Formato de Requerimiento'
        verbose_name_plural = 'Formatos de Requerimientos'

