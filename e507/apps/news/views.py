from django.shortcuts import render, get_object_or_404

import e507.apps.news.models


def home_view(request):
    latest_news_list = e507.apps.news.models.News.objects.order_by('-start_date')[:5]
    return render(request, 'news/home.html', {
        'latest_news_list': latest_news_list
    })


def detail_view(request, news_id):
    news = get_object_or_404(e507.apps.news.models.News, pk=news_id)
    return render(request, 'news/detail.html', {
        'news': news
    })
