from django.db import models

# Create your models here.
LEVEL = (
    ('1','1'),
    ('2','2'),
    ('3','3'),
    ('4','4'),
)

DEPARTMENT = (
    ('CS','CS'),
    ('IT','IT'),
)

GENDER = (
    ('Male','Male'),
    ('Female','Female'),
)

def image_upload(instance, filename):
    imagename , extension = filename.split(".")
    return "Students-Register/%s.%s"%(instance.id, extension)


class StudentRegisteration(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    student_id = models.IntegerField(default=1)
    level = models.CharField(max_length=15, choices=LEVEL)
    department = models.CharField(max_length=50, choices=DEPARTMENT)
    gender = models.CharField(max_length=20, choices=GENDER)
    image = models.ImageField(upload_to = image_upload)

    def __str__(self):
        return self.first_name

