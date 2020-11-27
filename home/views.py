from django.shortcuts import render, HttpResponse

# Create your views here.
from home.models import Setting, ContactMessage, CotactForm
from post.models import *
from django.contrib import messages
from django.http import HttpResponseRedirect


def index(request):
    setting = Setting.objects.all()
    category = Category.objects.all()
    article_slider = Article.objects.all().order_by('id')[:4]
    article_latest = Article.objects.all().order_by('-id')[:4]
    article_picked = Article.objects.all().order_by('?')[:4]

    page = "home"
    context = {
        'setting': setting,
        'category': category,
        'page': page,
        'article_slider': article_slider,
        'article_latest': article_latest,
        'article_picked': article_picked,

    }
    return render(request, 'index.html', context)

def about(request):
    setting = Setting.objects.all()
    category = Category.objects.all()
    context = {
        'setting': setting,
        'category': category,
    }
    return render(request, 'about.html', context)

def contact(request):
    if request.method == 'POST':
        form = CotactForm(request.POST)
        if form.is_valid():
            data = ContactMessage()
            data.name = form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request, "sizning murojatingiz qabul qilindi")
            return HttpResponseRedirect('/contact/')
    setting = Setting.objects.all()
    form = CotactForm
    category = Category.objects.all()
    context = {
        'setting': setting, 'form': form, 'category': category,
    }
    return render(request, 'contact.html', context)


def category_article(request, id, slug):
    category = Category.objects.all()
    catdata = Category.objects.get(pk=id)
    post = Article.objects.filter(category_id=id)
    context = {
        'category': category,
        'catdata': catdata,
        'post': post,
    }
    return render(request, 'category_article.html', context)


def post_detail(request, id, slug):
    category = Category.objects.all()
    post = Article.objects.filter(pk=id)
    comment = Comment.objects.filter(article_id=id)
    images = Images.objects.filter(article_id=id)
    context = {
        'category': category,
        'comment': comment,
        'post': post,
        'images': images,
    }
    return render(request, 'article_detail.html', context)
