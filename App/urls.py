from django.urls import path
from App import views as app_view


urlpatterns = [
    path('test', app_view.TestApi.as_view(), name='test')
]