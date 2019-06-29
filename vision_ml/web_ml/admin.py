from .models import ImageUploadModel
from django.contrib import admin

class upload_image_Admin(admin.ModelAdmin):
    list_display = ('description', 'document')


admin.site.register(ImageUploadModel, upload_image_Admin)