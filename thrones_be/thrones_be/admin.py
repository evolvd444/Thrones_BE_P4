from django.contrib import admin

# Register your models here.
from .models import Bathroom, Review, Tag, ImageUpload

admin.site.register(Bathroom)
admin.site.register(Review)
admin.site.register(Tag)
admin.site.register(ImageUpload)