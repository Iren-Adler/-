"""
переходим в сеттингс
медиа-рут и медиа-юрл, которые определяют пути прохождения и нахождения наших медиа файлов
прописать MEDIA_ROOT = os.path.join(BASE_DIR, )#место, в котором будем сохранять наши файлы
пометить my_site корневой папкой(синей)
импортировать os.path в сеттинге (не надо)
прописать медиа-юрл ____MEDIA_URL = 'media/' #по аналогии со статик, там где мы будем искать путь до нашх файлов
когда будем деплоить проект, нужно убрать дебаг = тру
вовремя дебага, фотографии не будут отображаться, поэтому нужно перейти в ЮРЛс корневой
в urlpatterns прописать_____path('', include('news.urls')), ((не забыть вкл include
импортировать _____from django.conf.urls.static import static
              _____from django.conf import settings
для режима дебаг предусмотреть сохранение? файлов
     if settings.DEBUG:
       urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)

переходим в файл views
from django.http import HttpResponse
from . import models

5.10
def index(request):
   news = models.News.objects.all()
    result = '<h1>Список новостей</h1>'
    for item in news:
        result += f'<div>\n<p>{item.title}</p>\n<p>{item.content}</p>\n</div>\n<hr>\n'
   return HttpResponse(result)
Вся лажа была в настройке ЮРЛС, надо было зарегать в сеттинге наше приложение,
дать в ЮРЛЕ новостей путь для функции индекс из вьюхи
в ЮРЛЕ my_site в юрлпаттернах добавить юрл новостей
чтобы был самый простой путь - надо просто '' оставить вместо пути
закачать пиллоу, сделать миграцию, создать суперпользователя, через админку добавить новости
в новостях создать папку шаблонов
в папке шаблонов создать папку ньюс
добавить html файл, назвать так же как и вьюха index
прописываем заголовки
убираем мясо с вьюхи
будем пользоваться функцией render(request, templ_name, contex_, django.shortcuts)
return render(request, 'news/index.html', {'news': news, 'title': 'Список  новостей'})
записать теги в html
в сеттинге поменять на русский
перейти в гет боотстрап -> docs -> выбрать 2-ой шаблон, там где есть cdn
всё удаляем в аштмл, вместо хелло, ворд вставляем наш титл
заходим в navbarv- первый шаблон
можно легко отформатировать с помошью соч-я клавиш ctrl alt L

убрать блок коллабса и кнопку, прописать титл
отформатировать
зайти в блок карточек в бутстрапе
вставить отформатировать
применить фильтры ____|
отформатировать
распечатать модуль категория
сделать миграцию и столкнуться с ошибкой - решение написать null=True
в админку добавить представление моделей
добавить категории через админку, отформотировать штмл
#
#ПРОДОЛЖЕНИЕ УРОКА ПО ШАБЛОНАМ
#
Чтобы добавить переключение по категориям, нужно в вьюхе в функции добавить поле categories = models.Category.objects.()
    context = {
        'news': news,
         'categories': categories,
        'title': 'Список новостей',
    }
    return render(request, 'news/index.html', context=context)
list group (bootstrap) - левая колоночка для категорий
форматирование
пишем представление еще для одной функции

def get_category(request, category_id):
    news = models.News.objects.filter(category_id=category_id)
    categories = models.Category.objects.all()
    category = models.Category.objects.get(pk=category_id)
    context = {
        'news': news,
        'categories': categories,
        'category': category,
    }
    return render(request, 'news/category.html', context=context)
Создадим еще один шаблон
Вставим всё из шаблона индекса
Вставим путь до категории href="/category/{{category.pk}}" pk (айдишник)
форматируем(в штмл индекса и категории)


ПРОБУЕМ С НАСЛЕДОВАНИЕМ
В базовой папке созадать templates, в ней base.html
свернуть блоки col-md-3 col-md-9 title (панелька с категориями и новости)
обернуть их в подписанные блоки

в индексе прописать {% extends 'base.html' %} раскрыть наследуемые блоки, прописать
убрать лишнее

создать папку inc в корневой папке проекта с шаблонами
В ней расписать навбар, в base убрать навбар и вставить {% include 'inc/_navbar.html' %}
В сеттинге шаблонов - 'DIRS': [os.path.join(BASE_DIR, 'templates')],
"""