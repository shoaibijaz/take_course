from django.db import models
from app_categories.models import Category
from django.conf import settings

class Course(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='courses_created', on_delete=models.DO_NOTHING)
    subject = models.ForeignKey(Category, related_name='course_category', null=True, on_delete=models.DO_NOTHING)
    instructor = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='courses_instructor',null=True, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=500)
    slug = models.SlugField(max_length=600, unique=True)
    description = models.TextField(blank=True)
    short_title = models.TextField(blank=True)
    intro_video = models.TextField(blank=True)
    summary = models.TextField(blank=True)
    lang = models.TextField(blank=True)
    tags = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    original_price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    order = models.IntegerField(default=0, null=True, blank=True)
    image = models.ImageField(upload_to='course_images/%Y/%m', default='images/default.png')
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "app_courses"

    def __str__(self):
        return self.title


class Module(models.Model):
    course = models.ForeignKey(Course, related_name='modules', on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=300)
    slug = models.SlugField(max_length=400)
    description = models.TextField(blank=True)
    order = models.IntegerField(default=0, null=True, blank=True)

    class Meta:
        db_table = "app_course_modules"

    def __str__(self):
        return self.title