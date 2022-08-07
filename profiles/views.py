from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.filters import SearchFilter
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from profiles.models import UserProfile
from profiles.serializers import HelloSerializer, UserProfileSerializer
from profiles.permissions import UpdateOwnProfile

#
# APIView: Usa metodos estandar [GET,POST]
# - Bueno para logica compleja.
# - Llamar a otros APIs.
# - Trabajar con archivos locales.
#
#
# Cuando usar las APIView:
# - Si se necesita control de la logica que debe llegar al Frontend.
# - Proceso de archivos y renderizar respuesta sincronizada.
# - Llamar a otros APIs/Servicios.
# - Acceso en archivos locales o datos.


# class HelloAPIView(APIView):
#     """ Primera vista de ejemplo """
#     serializer_class = HelloSerializer

#     def get(self, request, format=None):
#         """ Return List of Characteristics """
#         list  = [
#             'lkalf;lka;asjkdksdksldjklsjdljjd',
#             'akhsioieljlkadlkjsdjlsa,falfldllask',
#             'asdhkshdiluweoqueoijklcnzcn,mczbjj',
#             'akshdkjashdkhkadhhiuwehiwueioquoe',
#         ]
#         dic = {
#             'message' : 'Hello World!',
#             'list_text' : list
#         }
#         return Response(data=dic, status=HTTP_200_OK, content_type='application/json')

#     def post(self, request):
#         """ Create a Message """
#         serializer = self.serializer_class(data=request.data)

#         if serializer.is_valid():
#             name = serializer.validated_data.get('name')
#             message = f'Hello {name}'
#             return Response(data={'message': message}, status=HTTP_201_CREATED)

#         else:
#             return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

#     def retrieve(self, request, pk=None):
#         """ Retrieve Message """
#         return Response(data={'http_method' : 'GET'})

#     def update(self, request, pk=None):
#         """ Update Message """
#         return Response(data={'http_method': 'PUT'})

#     def partial_update(self, request, pk=None):
#         """ Patch Message """
#         return Response(data={'http_method': 'PATCH'})

#     def destroy(self, request, pk=None):
#         """ Delete Message """
#         return Response(data={'http_method': 'DELETE'})


class UserProfileViewSet(ModelViewSet):
    """ ViewSet For User Profile """
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (UpdateOwnProfile,)
    filter_backends = (SearchFilter,)
    search_fields = ('name', 'email')


class UserLogin(ObtainAuthToken):
    """ Create a new auth token for user """
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES