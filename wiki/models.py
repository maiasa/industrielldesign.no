from django.db import models
from django.template.defaultfilters import slugify
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFit
import datetime

from django.core.mail import send_mail

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=150, unique=True);
    introduction  = models.TextField(max_length=255, blank=True, null=True);
    body_text = models.TextField();
    
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=False)
    
    slug = models.SlugField(max_length=60, blank=True)
    visits = models.IntegerField(default=0);
    # image = ProcessedImageField(upload_to='wiki/',processors=[ResizeToFit(2000, 2000, False)], format='JPEG', options={'quality': 85})
    editable = models.BooleanField(default=True)

    class Meta:
        ordering = ['-visits', 'title']

    def save(self, *args, **kwargs):
        if not self.id:
            #Only set the slug when the object is created.
            self.slug = slugify(self.title) # Does not update to make sure links doesn't get broken
        super(Article, self).save(*args, **kwargs)

    def __str__(self):
        return self.title