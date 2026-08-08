from django.db import models




class Images(models.Model):
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
        if self.image:
            self.file_size = self.image.size
            self.width = self.image.width
            self.height = self.image.height
            
            # Calculate the file hash
            import hashlib
            hasher = hashlib.sha1()
            for chunk in self.image.chunks():
                hasher.update(chunk)
            self.file_hash = hasher.hexdigest()
        super().save(*args, **kwargs)
    class Meta:
        db_table = 'media_images'