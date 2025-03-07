from django.db import models
from django.conf import settings
from django.urls import reverse
from django.dispatch import receiver
from django.utils.text import slugify

import os
import uuid

# Choices
product_types = (
    ('pin_header', '排针'),
    ('female_header', '排母'),
    ('box_header', '简牛'),
    ('ejector_header', '牛角'),
    ('socket', '网口'),
    ('jumper', '短路帽'),
    ('fc', 'FC'),
    ('round_header', '圆孔针'),
    ('round_female_header', '圆孔座'),
    ('ic_socket', 'IC座'),
    ('din', '欧式插座'),
    ('plcc', 'plcc'),
    ('edge', '总线金手指'),
)

pitch = (
    ('0.8', '0.8'),
    ('1.0', '1.0'),
    ('1.27', '1.27'),
    ('2.0', '2.0'),
    ('2.54', '2.54'),
    ('3.81', '3.81'),
    ('5.0', '5.0'),
    ('5.08', '5.08'),
)

shape = (
    ('180', '180度'),
    ('90', '90度'),
    ('180/90', '180度/90度'),
    ('SMT', 'SMT'),
    ('HSMT', '卧贴'),
    ('CENT', '蜈蚣脚'),
    ('straddle', '夹板式'),
    ('U', 'U型')
)

row_num = (
    ('1', '单排'),
    ('2', '双排'),
    ('1/2', '单/双排'),
    ('3', '三排'),
    ('4', '四排'),
    ('5', '五排'),
)

pnum = (
    ('1', '单塑'),
    ('2', '双塑'),
    ('2+', '双塑以上'),
)

# Functions
def getPictureImagePath(instance, filename):
    return os.path.join('picture', str(instance.name), filename)


def getBluePrintPath(instance, filename):
    return os.path.join('blueprint', str(instance.name), filename)


def getProductPath(instance, filename):
    return os.path.join('product', str(instance.name), filename)


def getNewsPicture(instance, filename):
    return os.path.join('newspicture', str(instance.id), filename)

# Models
class Product(models.Model):
    name = models.CharField(max_length=100, unique=True) #chinese
    description = models.TextField(max_length=500, null=True, blank=True)
    en_name = models.CharField(max_length=100, unique=True, null=True, blank=True) #english
    en_description = models.TextField(max_length=500, null=True, blank=True)
    es_name = models.CharField(max_length=100, unique=True, null=True, blank=True) #spanish
    es_description = models.TextField(max_length=500, null=True, blank=True)
    de_name = models.CharField(max_length=100, unique=True, null=True, blank=True) #german
    de_description = models.TextField(max_length=500, null=True, blank=True)
    fr_name = models.CharField(max_length=100, unique=True, null=True, blank=True) #french
    fr_description = models.TextField(max_length=500, null=True, blank=True)
    ja_name = models.CharField(max_length=100, unique=True, null=True, blank=True) #japan
    ja_description = models.TextField(max_length=500, null=True, blank=True)
    ko_name = models.CharField(max_length=100, unique=True, null=True, blank=True) #korean
    ko_description = models.TextField(max_length=500, null=True, blank=True)
    ru_name = models.CharField(max_length=100, unique=True, null=True, blank=True) #russian
    ru_description = models.TextField(max_length=500, null=True, blank=True)
    slug = models.SlugField(max_length=150, unique=True, blank=True, verbose_name="URL Slug")
    pitch = models.CharField(max_length=20, choices=pitch, null=True, blank=True)
    picture = models.FileField(upload_to=getProductPath, null=True, blank=True)
    picture2 = models.FileField(upload_to=getProductPath, null=True, blank=True)
    picture3 = models.FileField(upload_to=getProductPath, null=True, blank=True)
    blueprint = models.FileField(upload_to=getProductPath, null=True, blank=True)
    pdf = models.FileField(upload_to=getProductPath, null=True, blank=True)
    product_type = models.CharField(max_length=50, choices=product_types, null=True, blank=True)
    row = models.CharField(max_length=10, null=True, blank=True, choices=row_num)
    pnum = models.CharField(max_length=10, null=True, blank=True, choices=pnum)
    shape = models.CharField(max_length=20, null=True, blank=True, choices=shape)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.en_name, allow_unicode=True)
        super().save(*args, **kwargs)

    def get_detail_url(self):
        return reverse(self.product_type+'_detail', args=[str(self.slug)])

    def __str__(self):
        return '%s' % (self.name)

# 更换文件时删除老的文件    
@receiver(models.signals.pre_save, sender=Product)
def execute_pre_save(sender, instance, *args, **kwargs):
    try:
        old = Product.objects.get(id=instance.id)
    except:
        return
    for field in old._meta.fields:
        if field.get_internal_type() == 'FileField' or field.get_internal_type() == 'ImageField':
            old_path = getattr(old, field.name)
            new_path = getattr(instance, field.name)
            if old_path != new_path:
                absolute_path = os.path.join(settings.MEDIA_ROOT, str(old_path))
                try:
                    os.remove(absolute_path)
                except:
                    pass


class News(models.Model):
    title = models.CharField(max_length=100, unique=True)
    content = models.TextField(max_length=2000, null=True, blank=True, unique=True)
    en_title = models.CharField(max_length=100, null=True, blank=True, unique=True)
    en_content = models.TextField(max_length=2000, null=True, blank=True, unique=True)
    es_title = models.CharField(max_length=100, null=True, blank=True, unique=True)
    es_content = models.TextField(max_length=2000, null=True, blank=True, unique=True)
    de_title = models.CharField(max_length=100, null=True, blank=True, unique=True)
    de_content = models.TextField(max_length=2000, null=True, blank=True, unique=True)
    fr_title = models.CharField(max_length=100, null=True, blank=True, unique=True)
    fr_content = models.TextField(max_length=2000, null=True, blank=True, unique=True)
    ja_title = models.CharField(max_length=100, null=True, blank=True, unique=True)
    ja_content = models.TextField(max_length=2000, null=True, blank=True, unique=True)
    ko_title = models.CharField(max_length=100, null=True, blank=True, unique=True)
    ko_content = models.TextField(max_length=2000, null=True, blank=True, unique=True)
    ru_title = models.CharField(max_length=100, null=True, blank=True, unique=True)
    ru_content = models.TextField(max_length=2000, null=True, blank=True, unique=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=True, null=True, blank=True)
    slug = models.SlugField(max_length=150, unique=True, blank=True, verbose_name="URL Slug")

    def save(self, *args, **kwargs):
        self.slug = slugify(self.en_title, allow_unicode=True)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('news_detail', args=[str(self.slug)])

    def __str__(self):
        return '%s' % (self.title)