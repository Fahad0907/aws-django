from celery import shared_task
from App import models as app_model


@shared_task(bind=True)
def test_func(self):
    app_model.A.objects.create(name='haha')
    return "done"
