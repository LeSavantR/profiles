from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.filters import SearchFilter
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.settings import api_settings

from profiles.models import UserProfile
from profiles.serializers import UserProfileSerializer
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

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data, context={'request' : request}
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response(
            {
                'token' : token.key,
                'created' : created,
                'user_id' : user.pk,
                'username' : user.email,
                'message' : f'Welcome, {user.name}'
            },
            status=HTTP_200_OK,
            content_type='application/json'
        )


class UserLogout(APIView):
    """ Destroy a user token """

    def get(self, request, format=None):
        """ Logout a user """
        request.user.auth_token.delete()
        message = {'message' : 'User Logout'}
        return Response(data=message, status=HTTP_200_OK)