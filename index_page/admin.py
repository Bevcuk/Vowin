from django.contrib import admin

# Register your models here.
from index_page.models import Image, TypeImage

admin.site.register(Image)
admin.site.register(TypeImage)
