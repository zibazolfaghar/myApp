import os

from django.db import models


# Create your models here.


def get_filename_ext(filepath):
    base_name=os.path.basename(filepath)
    name,ext=os.path.splitext(base_name)
    return name , ext
def uplad_image_path(instance,filename):
    name,ext=get_filename_ext(filename)
    final_name=f"{instance.id}-{instance.title}{ext}"
    return f"sliders/{final_name}"

class Slider(models.Model):
    title=models.CharField(max_length=120,verbose_name='عنوان')
    link=models.URLField(verbose_name='آدرس')
    description=models.TextField(verbose_name='توضیحات')
    image = models.ImageField(upload_to=uplad_image_path, null=True, blank=True, verbose_name='تصویر')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'اسلایدر'
        verbose_name_plural = 'اسلایدرها'