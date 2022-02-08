from main.tasks import home_download
from django.http import HttpResponse


def home(request):
    home_download.delay()
    return HttpResponse('<h1>Celery+Django+Docker/DownloadWorker</h1>')





