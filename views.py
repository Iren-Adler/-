from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from . import models
#5.10
def index(request):
    news = models.News.objects.all()
    categories = models.Category.objects.all()
    context = {
        'news': news,
        'categories': categories,
        'title': 'Список новостей',
    }
    return render(request, 'news/index.html', context=context)


def get_category(request, category_id):
    news = models.News.objects.filter(category_id=category_id)
    categories = models.Category.objects.all()
    category = models.Category.objects.get(pk=category_id)#ПЕРВИЧНЫЙ КЛЮЧ
    context = {
        'news': news,
        'categories': categories,
        'category': category,
    }
    return render(request, 'news/category.html', context=context)
