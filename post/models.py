from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.forms import ModelForm
from django.utils.safestring import mark_safe

from ckeditor_uploader.fields import RichTextUploadingField
class Category(models.Model):
    title = models.CharField(max_length=255)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    slug = models.SlugField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title

class Article(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    author = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to='images/', blank=True)
    detail = RichTextUploadingField()
    slug = models.SlugField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/').format(self.image.url)
    image_tag.short_description = 'image'

    def avaragereview(self):
        reviews = Comment.objects.filter(product=self, status='Mavjud').aggregate(avarage=Avg('rate'))
        avg = 0
        if reviews["avarage"] is not None:
            avg = float(reviews["avarage"])
        return avg

    def countreview(self):
        reviews = Comment.objects.filter(product=self, status='Mavjud').aggregate(avarage=Count('id'))
        cnt = 0
        if reviews["count"] is not None:
            cnt = int(reviews["count"])
        return cnt
class Images(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, blank=True)
    image = models.ImageField(blank=True, upload_to='images/')

    def str(self):
        return self.title


class Comment(models.Model):
    STATUS = (
        ('Mavjud', 'Mavjud'),
        ('Mavjud emas', 'Mavjud emas'),

    )
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=55, blank=True)
    comment = models.TextField(max_length=500, blank=True)
    rate = models.IntegerField(default=1)
    ip = models.CharField(max_length=20, blank=True)
    status = models.CharField(max_length=25, choices=STATUS, default='Mavjud')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.subject

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['subject', 'comment', 'rate']
