from django.contrib import admin
from .models import BlogComment,Blog
# Register your models here.
admin.site.register(Blog)
admin.site.register(BlogComment)
