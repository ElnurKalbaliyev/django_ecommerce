# ecommerce/celery.py

import os
from celery import Celery
import dotenv

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ecommerce.settings")
dotenv.load_dotenv()
app = Celery("ecommerce")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()