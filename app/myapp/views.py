from django.core.files.storage import FileSystemStorage
from django.views.generic import View
from django.http import JsonResponse
from django.shortcuts import render


def health_check(request):
    return JsonResponse({'status': 'ok'})


class UploadMediaFile(View):

    def get(self, request, *args, **kwargs):
        return render(request, "myapp/upload_media_file.html")

    def post(self, request, *args, **kwargs):

        file = request.FILES["file"]
        fs = FileSystemStorage()

        file = fs.save(file.name, file)
        file_url = fs.url(file)

        context = {
            "file_url": file_url
        }

        return render(request, "myapp/upload_media_file.html", context)
