from django.db import models
from django.conf import settings
from django.urls import reverse
from django.dispatch import receiver
from django.utils.text import slugify
from django.utils import timezone

import os
import uuid


# Choices
product_types = (
    ('pin-header', '排针'),
    ('female-header', '排母'),
    ('box-header', '简牛'),
    ('ejector-header', '牛角'),
    ('socket', '网口'),
    ('jumper', '短路帽'),
    ('idc-cable-connector', 'FC'),
    ('round-header', '圆孔针'),
    ('round-female-header', '圆孔座'),
    ('ic-socket', 'IC座'),
    ('din41612', '欧式插座'),
    ('plcc', 'plcc'),
    ('edge-card-connector', '总线金手指'),
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
def getProductPath(instance, filename):
    return os.path.join('product', str(instance.id), filename)


def getNewsPath(instance, filename):
    return os.path.join('news', str(instance.id), filename)

# Models
class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(max_length=500, null=True, blank=True)
    seo_description = models.TextField(max_length=300, null=True, blank=True)
    slug = models.SlugField(max_length=150, unique=True, blank=True, verbose_name="URL Slug")
    pitch = models.CharField(max_length=20, choices=pitch, null=True, blank=True)
    picture = models.FileField(upload_to=getProductPath, null=True, blank=True)
    picture2 = models.FileField(upload_to=getProductPath, null=True, blank=True)
    picture3 = models.FileField(upload_to=getProductPath, null=True, blank=True)
    pdf = models.FileField(upload_to=getProductPath, null=True, blank=True)
    product_type = models.CharField(max_length=50, choices=product_types, null=True, blank=True)
    row = models.CharField(max_length=10, null=True, blank=True, choices=row_num)
    pnum = models.CharField(max_length=10, null=True, blank=True, choices=pnum)
    shape = models.CharField(max_length=20, null=True, blank=True, choices=shape)
    created_at = models.DateTimeField(default=timezone.now, editable=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name_en, allow_unicode=True)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse(self.product_type+'-detail', args=[str(self.slug)])

    # def get_detail_url(self):
    #     return reverse(self.product_type+'-detail', args=[str(self.slug)])

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
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    title = models.CharField(max_length=100, unique=True)
    content = models.TextField(max_length=2000, null=True, blank=True)
    seo_description = models.TextField(max_length=300, null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now, editable=True, null=True, blank=True)
    picture = models.FileField(upload_to=getNewsPath, null=True, blank=True)
    about = models.CharField(max_length=50, choices=product_types, null=True, blank=True)
    slug = models.SlugField(max_length=150, unique=True, blank=True, verbose_name="URL Slug")

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title_en, allow_unicode=True)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('news-detail', args=[str(self.slug)])

    # def get_detail_url(self):
    #     return reverse('news-detail', args=[str(self.slug)])

    def __str__(self):
        return '%s' % (self.title)
    
# 更换文件时删除老的文件    
@receiver(models.signals.pre_save, sender=News)
def execute_pre_save_news(sender, instance, *args, **kwargs):
    try:
        old = News.objects.get(id=instance.id)
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