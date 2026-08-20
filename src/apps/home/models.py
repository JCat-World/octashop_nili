from django.db import models
from django.utils.translation import gettext_lazy as _

def slider_directory_path(instance, filename):
    return 'images/sliders/{0}/{1}'.format(instance.id, filename)


class TopSliderModel(models.Model):
    product = models.ForeignKey(
        'catalogs.Product', on_delete=models.CASCADE, null=False, related_name="top_sliders")
    link = models.URLField(_("آدرس"), null=True, blank=True)
    title = models.CharField(_("تایتل"), max_length=50)
    image = models.ImageField(_("اسلایدر بالا"), upload_to=slider_directory_path,
                              height_field=None, width_field=None, max_length=None)

    class Meta:
        # db_table = ''
        # managed = True
        verbose_name = 'اسلایدر بالا'
        verbose_name_plural = 'اسلایدرهای بالا'

    def __str__(self):
        return self.title
    