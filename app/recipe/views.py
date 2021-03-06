from rest_framework import viewsets, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import Tag
from . import serializer


class TagViewSet(viewsets.GenericViewSet, mixins.ListModelMixin,
                mixins.CreateModelMixin):
    ''' Manage tags in database '''
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Tag.objects.all()
    serializer_class = serializer.TagSerializer

    def get_queryset(self):
        ''' Return objects for current authenticated user only '''
        return self.queryset.filter(user=self.request.user).order_by('-name')

    def perform_create(self, serializer):
        ''' Create a new Tag '''
        serializer.save(user=self.request.user)
