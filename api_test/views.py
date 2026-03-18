from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Content
from .serializers import ContentSerializer


class ContentViewSet(ModelViewSet):
    serializer_class = ContentSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Content.objects.all()

        title = self.request.query_params.get('title')
        desc = self.request.query_params.get('desc')

        if title:
            queryset = queryset.filter(title__icontains=title)

        if desc:
            queryset = queryset.filter(desc__icontains=desc)

        return queryset