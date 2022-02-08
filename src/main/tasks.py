import requests as r
import uuid
from django.conf import settings
from celery import shared_task

catUrl = "https://cataas.com/cat"


@shared_task
def home_download():
    resp = r.get(catUrl)
    print(resp)
    file_ext = resp.headers.get('Content-type').split('/'[1])
    print(file_ext)
    file_name = settings.BASE_DIR / 'cats' / (str(uuid.uuid4())) + " " + file_ext
    print(file_name)
    with open(file_name, 'wb') as f:
        for _ in resp.iter_content(chunk_size=128):
            f.write(_)
    return True
