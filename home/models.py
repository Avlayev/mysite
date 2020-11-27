from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.forms import ModelForm, TextInput, Textarea, EmailInput

# Create your models here.
class Setting(models.Model):
    title = models.CharField(max_length=255)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    about = RichTextUploadingField()
    contact = RichTextUploadingField()
    facebook = models.CharField(max_length=255, blank=True)
    instagram = models.CharField(max_length=255, blank=True)
    telegram = models.CharField(max_length=255, blank=True)
    youtube = models.CharField(max_length=255, blank=True)
    tiktok = models.CharField(max_length=255, blank=True)
    gmail = models.EmailField(max_length=255, blank=True)
    email = models.EmailField(max_length=255, blank=True)
    twitter = models.CharField(max_length=255, blank=True)
    def __str__(self):
        return self.title

class ContactMessage(models.Model):
    STATUS = (
        ('Yangi', 'Yangi'),
        ("O'qildi", "O'qildi"),
        ('Yopilgan', 'Yopilgan'),

    )
    name = models.CharField(blank=True, max_length=255)
    email = models.EmailField(blank=True, max_length=255)
    subject = models.CharField(blank=True, max_length=255)
    message = models.TextField(blank=True, max_length=255)
    status = models.CharField(max_length=255, choices=STATUS,default='Yangi',)
    ip = models.CharField(blank=True, max_length=255)
    note = models.CharField(blank=True, max_length=255)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class CotactForm(ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': TextInput(attrs={'class':"input", 'placeholder':'Ism Sharifingiz'}),
            'email': EmailInput(attrs={'class': "input", 'placeholder': 'Email mazmuni'}),
            'subject': TextInput(attrs={'class': "input", 'placeholder': 'Murojaat mazmuni'}),
            'message': Textarea(attrs={'class': "input", 'placeholder': 'Murojaat matni','rows':'5'}),

        }


