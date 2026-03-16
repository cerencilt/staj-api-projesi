from django.db import models


LANGUAGE_CHOICES = [
    ("tr", "Turkish"),
    ("en", "English"),
    ("es", "Spanish"),
    ("ar", "Arabic"),
]

class Content(models.Model):

    title = models.CharField(max_length=150)
    desc = models.TextField(default="")

    cover = models.ImageField(upload_to="covers/", default="covers/default.jpg")

    source = models.URLField()
    clean_source = models.URLField(null=True, blank=True)

    languages = models.CharField(
    max_length=2,
    choices=LANGUAGE_CHOICES
)

subtitles = models.CharField(
    max_length=2,
    choices=LANGUAGE_CHOICES,
    blank=True
)

created = models.DateTimeField(auto_now_add=True)
publish = models.DateTimeField(null=True, blank=True)

draft = models.BooleanField(default=True)

def __str__(self):
        return self.title