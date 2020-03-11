from django.db import models
from django.conf import settings

class Category(models.Model):

    name = models.CharField(max_length=250, blank=True, unique=True, null=True)
    title = models.CharField(max_length=300, blank=True, null=True)
    slug = models.SlugField(max_length=300, blank=True, null=True)
    image = models.CharField(max_length=200, blank=True, null=True)
    icon = models.CharField(max_length=100, blank=True, null=True)
    details = models.CharField(max_length=300, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='category_created', on_delete=models.DO_NOTHING)
    parent = models.ForeignKey('self', null=True, related_name='parent_category', on_delete=models.DO_NOTHING)
    
    class Meta:
        db_table = "app_categories"

    def __str__(self):
        return self.name