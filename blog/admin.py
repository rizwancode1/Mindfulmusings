from django.contrib import admin
from .models import Categories,  Tag , Article, Comment
# Register your models here.

admin.site.register(Categories)
admin.site.register(Tag)
admin.site.register(Article)
admin.site.register(Comment)
