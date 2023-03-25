from django.db import models
from django.core.validators import validate_image_file_extension
# Create your models here.
class File(models.Model):
    img = models.ImageField(verbose_name=("Upload Image"), upload_to="osteo/images",validators=[validate_image_file_extension])
