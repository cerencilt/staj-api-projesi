from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.core.cache import cache
from django.conf import settings
from .models import Content
from .serializers import ContentSerializer


CONTENT_CACHE_KEY = 'content_list'


class ContentViewSet(ModelViewSet):
    serializer_class = ContentSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        title = self.request.query_params.get('title')
        desc = self.request.query_params.get('desc')

       
        if title or desc:
            queryset = Content.objects.all()
            if title:
                queryset = queryset.filter(title__icontains=title)
            if desc:
                queryset = queryset.filter(desc__icontains=desc)
            return queryset

        cached = cache.get(CONTENT_CACHE_KEY)
        if cached is not None:
            
            return cached
        
        queryset = Content.objects.all()
        cache.set(CONTENT_CACHE_KEY, queryset, settings.CACHE_TTL)
        return queryset 