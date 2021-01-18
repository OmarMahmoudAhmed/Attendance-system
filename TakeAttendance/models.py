from django.db import models
from django.db.models.fields.files import ImageField




def image_upload(instance, filename):
    imagename , extension = filename.split(".")
    return "Students_Attendance/%s.%s"%(instance.id, extension)

# Create your models here.
class Attendance(models.Model):
    attendance_image = models.ImageField(upload_to = image_upload) 
    take_at = models.models.DateTimeField(auto_now=True)