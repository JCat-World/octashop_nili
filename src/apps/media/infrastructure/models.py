import hashlib

from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

from apps.media.exceptions import DuplicateImageException




class Image(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(width_field='width', height_field='height', upload_to='images/', null=True, blank=True)
    
    
    width = models.PositiveIntegerField(editable=False, null=True, blank=True)
    height = models.PositiveIntegerField(editable=False, null=True, blank=True)
    
    
    file_hash = models.CharField(max_length=40, null=True, blank=True,db_index=True)
    file_size = models.PositiveIntegerField(null=True, blank=True)
    
    focal_point_x = models.FloatField(null=True, blank=True)
    focal_point_y = models.FloatField(null=True, blank=True)
    
    focal_point_width = models.FloatField(null=True, blank=True)
    focal_point_height = models.FloatField(null=True, blank=True)
    
    def save(self, *args, **kwargs):
        if not self.image.file.closed:
            if self.image:
                self.file_size = self.image.size
                self.width = self.image.width
                self.height = self.image.height
 # Ensure the file is opened before reading
                hasher = hashlib.sha1()
                for chunk in self.image.chunks():
                    hasher.update(chunk)
                self.file_hash = hasher.hexdigest()
        super().save(*args, **kwargs)
    class Meta:
        db_table = 'media_images'
        
    # def __str__(self):
    #     return self.title
        
        
        

@receiver(pre_save, sender=Image)
def check_duplicate_hash(sender, instance, **kwargs):
    # TODO : fix this check to avoid race conditions
    existed = Image.objects.filter(file_hash=instance.file_hash).exclude(pk=instance.pk).exists()
    if existed:
        raise DuplicateImageException("Duplicate")