from django.http import HttpResponse, JsonResponse
from django.views import View


def hello(request):
    return HttpResponse('Hello World from function!')


class HelloView(View):
    def get(self, request):
        return HttpResponse('Hello World from class!')


def year_post(request, year):
    text = ""
    ...  # формируем статьи за год и месяц
    return HttpResponse(f'Posts from {year}<br>{text}')


class MonthPost(View):
    def get(self, request, year, month):
        text = ""
        ...  # формируем статьи за год и месяц
        return HttpResponse(f'Posts from {month}/{year}<br>{text}')
