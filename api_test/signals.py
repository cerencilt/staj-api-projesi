# api_test/signals.py
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.core.cache import cache
from .models import Content

CONTENT_CACHE_KEY = 'content_list'

@receiver(post_save, sender=Content)
def invalidate_cache_on_save(sender, **kwargs):
    cache.delete(CONTENT_CACHE_KEY)

@receiver(post_delete, sender=Content)
def invalidate_cache_on_delete(sender, **kwargs):
    cache.delete(CONTENT_CACHE_KEY) 