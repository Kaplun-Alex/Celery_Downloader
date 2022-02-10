from . import tasks
from django.http import HttpResponse


def home(request):
    tasks.home_download.delay()
    return HttpResponse('<h1>Celery+Django+Docker/DownloadWorker</h1>')





