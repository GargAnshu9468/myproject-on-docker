from django.http import JsonResponse, HttpResponse
from django.views.generic import View


def health_check(request):
    return JsonResponse({'status': 'ok'})


class Home(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('<h1 style="text-align: center;">Home Page</h1>')
