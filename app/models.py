from django.db import models
from django.dispatch.dispatcher import receiver
import os
# Create your models here.
class UploadModel(models.Model):
    file_id = models.AutoField(primary_key=True)
    date_of_upload = models.DateTimeField(auto_now_add=True)
    file = models.ImageField(upload_to='images')
    
    def __str__(self):
        return self.date_of_upload.isoformat()

def _delete_file(path):
    if os.path.isfile(path):
        os.remove(path)
        
@receiver(models.signals.post_delete, sender=UploadModel)
def delete_file(sender, instance, *args,**kwargs):
    if instance.file:
        _delete_file(instance.file.path)
