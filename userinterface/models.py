from django.db import models

# Create your models here.


class myuploadfile(models.Model):
    fName = models.CharField(max_length=255)
    myFile = models.FileField(upload_to="")

    def __str__(self):
        return self.fName
    

